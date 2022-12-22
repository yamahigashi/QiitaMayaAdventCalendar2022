# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

from maya import cmds  # NOQA

import traceback


# =============================================================================
def has_houdini_engine_installed():
    # type: () -> bool
    return True
    return "houdiniEngine" in cmds.pluginInfo(query=True, listPlugins=True)


def ensure_dx11_shader_loaded():
    # type: () -> None
    cmds.loadPlugin("dx11Shader.mll", quiet=True)


def ensure_exprespy_shader_loaded():
    # type: () -> None

    mod = os.getenv("MAYA_MODULE_PATH")
    pl = os.getenv("MAYA_PLUG_IN_PATH")
    v = cmds.about(version=True)

    for p in mod.split(";"):
        if "exprespy" in p:
            plug_ins = os.path.join(p, "plug-ins", "win64_{}".format(v)).replace(os.sep, "/")
            os.environ["MAYA_PLUG_IN_PATH"] += ";{}".format(str(plug_ins))

    cmds.loadPlugin("exprespy.mll", quiet=True)


def ensure_fbx_loaded():
    # type: () -> None

    cmds.loadPlugin("fbxmaya.mll", quiet=True)


def ensure_houdini_engine_loaded():
    # type: () -> None
    if has_houdini_engine_installed():

        # avoiding Qt*.pyd conflicts with houdiniEngine.mll
        from PySide2 import (  # noqa
            QtWidgets,
            QtGui,
            QtCore,
            QtNetwork,
            QtXml,
            QtHelp,
            QtUiTools,
            __version__
        )

        cmds.loadPlugin("houdiniEngine.mll")


def install_pyblish():
    # type: () -> None

    try:
        __import__("pyblish_maya")

    except ImportError:
        import traceback
        print ("pyblish-maya: Could not load integration: %s"
               % traceback.format_exc())

    else:
        import pyblish_maya
        pyblish_maya.setup()

    from maya import cmds
    from sagittarius_pyblish.pipeline import install
    from pyblish import api

    # Allow time for dependencies (e.g. pyblish-maya)
    # to be installed first.
    cmds.evalDeferred(lambda: install())
    cmds.evalDeferred(lambda: api.register_gui("pyblish_qml"))


# ============================================================================

def setup():

    try:
        ensure_dx11_shader_loaded()
    except RuntimeError:
        traceback.print_exc()

    try:
        ensure_exprespy_shader_loaded()
    except RuntimeError:
        traceback.print_exc()

    try:
        ensure_fbx_loaded()
    except RuntimeError:
        traceback.print_exc()

    try:
        # install_pyblish()
        pass
    except RuntimeError:
        traceback.print_exc()

    # conflict: multiprocessing
    # try:
    #     ensure_houdini_engine_loaded()
    # except RuntimeError:
    #     traceback.print_exc()
