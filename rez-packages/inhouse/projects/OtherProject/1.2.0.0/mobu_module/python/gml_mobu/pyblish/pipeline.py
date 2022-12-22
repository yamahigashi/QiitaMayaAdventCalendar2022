import os
import sys
import logging

from Qt import QtWidgets, QtGui  # type: ignore

from pyblish import api

if False:
    # For type annotation
    from typing import Any, Dict, List, Type, Text, Tuple  # NOQA
    from PyQt5 import QtCore, QtWidgets, QtGui  # NOQA

# import pyfbsdk as fb

# from . import lib

self = sys.modules[__name__]
self.log = logging.getLogger("pyblish-motionbuilder")
self.menu = "pyblishStarter"


def install():
    try:
        import pyblish_motionbuilder
        assert pyblish_motionbuilder.is_setup()

    except (ImportError, AssertionError):
        _display_missing_dependencies()

    _register_plugins()


def uninstall():
    _uninstall_menu()


def _uninstall_menu():
    widgets = dict((w.objectName(), w) for w in QtWidgets.qApp.allWidgets())
    menu = widgets.get(self.menu)

    if menu:
        menu.deleteLater()
        del(menu)


def _register_plugins():
    """Register accompanying plugins"""
    from . import plugins
    plugin_path = os.path.dirname(plugins.__file__)
    api.register_plugin_path(plugin_path)

    for directory in os.listdir(plugin_path):
        p = os.path.join(plugin_path, directory)

        if not os.path.isdir(p):
            continue
        api.register_plugin_path(os.path.abspath(p))

    # for path in PLUGIN_PATHS:
    #     self.log.info(path)
    #     api.register_plugin_path(path)


def _display_missing_dependencies():
        import pyblish

        messagebox = QtWidgets.QMessageBox()
        messagebox.setIcon(messagebox.Warning)
        messagebox.setWindowIcon(QtGui.QIcon(os.path.join(
            os.path.dirname(pyblish.__file__),
            "icons",
            "logo-32x32.svg"))
        )

        spacer = QtWidgets.QWidget()
        spacer.setMinimumSize(400, 0)
        spacer.setSizePolicy(QtWidgets.QSizePolicy.Minimum,
                             QtWidgets.QSizePolicy.Expanding)

        layout = messagebox.layout()
        layout.addWidget(spacer, layout.rowCount(), 0, 1, layout.columnCount())

        messagebox.setWindowTitle("Uh oh")
        messagebox.setText("Missing dependencies")

        messagebox.setInformativeText(
            "pyblish-star requires pyblish-motionbuilder.\n"
        )

        # TODO:
        messagebox.setDetailedText(
            "1) Install Pyblish for MotionBuilder\n"
            "\n"
            "$ pip install pyblish-motionbuilder\n"
            "\n"
            "2) Run setup()\n"
            "\n"
            ">>> import pyblish_motionbuilder\n"
            ">>> pyblish_motionbuilder.setup()\n"
            "\n"
            "3) Try again.\n"
            "\n"
            ">>> pyblish_star.install()\n"

            "See https://github.com/pyblish/pyblish-star "
            "for more information."
        )

        messagebox.setStandardButtons(messagebox.Ok)
        messagebox.exec_()

        raise RuntimeError("pyblish-star requires pyblish-motionbuilder"
                           "to have been setup.")
