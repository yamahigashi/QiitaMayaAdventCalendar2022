import os
import sys
import json
import errno
import types
import shutil
import logging
import tempfile
import contextlib

from maya import cmds

from pyblish import api

from . import plugins

if False:
    # For type annotation
    from typing import (
        # Optional,
        Dict,
        List,
        Tuple,
        # Pattern,
        # Callable,
        Any,
        Text,
        Union,
        Iterable,
        Generator
    )  # NOQA


self = sys.modules[__name__]

self.log = logging.getLogger("pyblish-sample")

self._registered_data = list()
self._registered_families = list()
self._registered_formats = list()
self._registered_root = os.getcwd()  # Default to current working directory
self._is_installed = False

PLUGINS_PATH = os.path.dirname(plugins.__file__)
PLUGIN_PATHS = [PLUGINS_PATH]

for subdir in ("workflow",
               "pipeline",
               "collector",
               "extractor",
               "integrator",
               "validator",

               "starter",
               "modeling",
               "lookdev",
               "animation",
               "rig",
               ):
    PLUGIN_PATHS.append(os.path.join(PLUGINS_PATH, subdir))


def default_host():
    """A default host, in place of anything better

    This may be considered as reference for the
    interface a host must implement. It also ensures
    that the system runs, even when nothing is there
    to support it.

    """

    host = types.ModuleType("default")
    host.__dict__.update({
        "ls": lambda: [],
        "load": lambda asset, version, representation: None,
        "create": lambda name, family: "my_instance",
    })

    return host


def debug_host():
    host = types.ModuleType("standalone")
    host.__dict__.update({
        "ls": lambda: [],
        "load": lambda asset, version=-1, representation=None:
            sys.stdout.write(json.dumps({
                "asset": asset,
                "version": version,
                "representation": representation
            }, indent=4) + "\n"),
        "create": lambda name, family:
            sys.stdout.write(json.dumps({
                "name": name,
                "family": family,
            }, indent=4))
    })

    return host


self._registered_host = default_host()


def install():
    try:
        import pyblish_maya
        assert pyblish_maya.is_setup()

    except (ImportError, AssertionError):
        pass
        # _display_missing_dependencies()

    # _register_formats()
    # _register_root()
    register_plugins()


def uninstall():
    _deregister_formats()


def _register_formats():
    api.register_format(".ma")
    api.register_format(".mb")
    api.register_format(".abc")
    api.register_format(".fbx")


def _deregister_formats():
    api.deregister_format(".ma")
    api.deregister_format(".mb")
    api.deregister_format(".abc")
    api.deregister_format(".fbx")


def _register_root():
    """Register project root or directory of current working file"""
    root = (
        cmds.workspace(rootDirectory=True, query=True) or
        cmds.workspace(directory=True, query=True)
    )

    api.register_root(root)


def is_installed():
    """Return state of installation

    Returns:
        True if installed, False otherwise

    """

    return self._is_installed


def register_default_data():
    register_data(key="id", value="pyblish.starter.instance")
    register_data(key="name", value="{name}")
    register_data(key="family", value="{family}")


def register_default_families():
    register_family(
        name="starter.model",
        help="Polygonal geometry for animation"
    )

    register_family(
        name="starter.rig",
        help="Character rig"
    )

    register_family(
        name="starter.animation",
        help="Pointcache"
    )


def register_root(path):
    """Register currently active root"""
    self._registered_root = path


def registered_root():
    """Return currently registered root"""
    return self._registered_root


# Alias
root = registered_root


def register_format(format):
    """Register a supported format

    A supported format is used to determine which of any available
    representations are relevant to the currently registered host.

    """

    self._registered_formats.append(format)


def register_host(host):
    missing = list()
    for member in ("load",
                   "create",
                   "ls",):
        if not hasattr(host, member):
            missing.append(member)

    assert not missing, (
        "Incomplete interface for host: '%s'\n"
        "Missing: %s" % (host, ", ".join(missing))
    )

    self._registered_host = host


def register_plugins():
    """Register accompanying plugins"""
    from . import plugins
    plugin_path = os.path.dirname(plugins.__file__)
    api.register_plugin_path(plugin_path)

    for directory in listdir(plugin_path):
        p = os.path.join(plugin_path, directory)

        if not os.path.isdir(p):
            continue
        api.register_plugin_path(os.path.abspath(p))

    for path in PLUGIN_PATHS:
        self.log.info(path)
        api.register_plugin_path(path)


def register_data(key, value, help=None):
    """Register new default attribute

    Arguments:
        key (str): Name of data
        value (object): Arbitrary value of data
        help (str, optional): Briefly describe

    """

    self._registered_data.append({
        "key": key,
        "value": value,
        "help": help or ""
    })


def register_family(name, data=None, help=None):
    """Register family and attributes for family

    Arguments:
        name (str): Name of family
        data (dict, optional): Additional data, see
            :func:`register_data` for docstring on members
        help (str, optional): Briefly describe this family

    """

    self._registered_families.append({
        "name": name,
        "data": data or [],
        "help": help or ""
    })


def registered_formats():
    return self._registered_formats[:]


def registered_families():
    return self._registered_families[:]


def registered_data():
    return self._registered_data[:]


def registered_host():
    return self._registered_host


def deregister_default_families():
    self._registered_families[:] = list()


def deregister_default_data():
    self._registered_data[:] = list()


def deregister_plugins():
    from . import plugins
    plugin_path = os.path.dirname(plugins.__file__)

    try:
        api.deregister_plugin_path(plugin_path)
    except ValueError:
        self.log.warning("pyblish-star plug-ins not registered.")


def deregister_formats():
    self._registered_formats[:] = list()


def deregister_host():
    self._registered_host = default_host()


def listdir(dirname):
    """Prefer empty list to OSError on os.listdir

    Example:
        >>> listdir("/definitely/does/not/exist")
        []
        >>> listdir(os.path.expanduser("~")) != []
        True

    """

    try:
        return os.listdir(dirname)
    except OSError as e:
        # Only handle missing directories
        if e.errno == errno.ENOENT:  # No such file or directory
            return list()
        raise


def gather_task_instances():
    # type: () -> Iterable[Dict[Text, Dict]]
    """Return yield pyblish assets information in current scene."""

    for objset in cmds.ls("*.id",
                          long=True,            # Produce full names
                          type="objectSet",     # Only consider objectSets
                          recursive=True,       # Include namespace
                          objectsOnly=True):    # Return objectSet, rather
                                                # than its members

        if not cmds.objExists(objset + ".id"):
            continue

        if not cmds.getAttr(objset + ".id") == "pyblish.starter.instance":
            continue

        # The developer is responsible for specifying
        # the family of each instance.
        if not cmds.objExists(objset + ".family"):
            self.log.warn("\"%s\" was missing a family" % objset)
            continue

        attributes = {"name": objset}

        # Apply each user defined attribute as data
        for attr in cmds.listAttr(objset, userDefined=True) or list():
            try:
                value = cmds.getAttr(objset + "." + attr)

            except Exception:
                # Some attributes cannot be read directly,
                # such as mesh and color attributes. These
                # are considered non-essential to this
                # particular publishing pipeline.
                value = None

            attributes[attr] = value

        yield {"name": objset, "attributes": attributes}


def gather_instances(prefix):

    import maya.cmds as cmds

    objset = cmds.ls(
        "{}_*.id".format(prefix),
        long=True,
        type="objectSet",
        recursive=True,
        objectsOnly=True
    )

    return objset



