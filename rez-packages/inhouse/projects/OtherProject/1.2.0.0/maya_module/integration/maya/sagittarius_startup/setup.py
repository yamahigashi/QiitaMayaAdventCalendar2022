# -*- coding: utf-8 -*-
# from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function

import os
import traceback
from logging import getLogger, WARN, DEBUG, INFO  # noqa

if False:
    # For type annotation
    from typing import Optional, Dict, List, Tuple, Pattern, Callable, Any, Text  # NOQA
###############################################################################

logger = getLogger(__name__)
logger.setLevel(WARN)
logger.setLevel(INFO)


SAGITTARIUS_STARTUP_FINISHED = False

###############################################################################


def setup():
    import byk_startup.setup
    byk_startup.setup.setup()

    global SAGITTARIUS_STARTUP_FINISHED

    import maya.cmds as cmds
    import maya.mel as mel

    logger.info("sagittarius startup setup start")

    if SAGITTARIUS_STARTUP_FINISHED:
        return

    try:
        from . import callback
        callback.setup()

    except Exception:
        logger.error("callback setup failed")
        traceback.print_exc()

    try:
        from . import plugins
        plugins.setup()

    except Exception:
        logger.error("plugins setup failed")
        traceback.print_exc()

    try:
        if not cmds.about(batch=True):
            from sagittarius_maya import menu
            menu.register()

    except Exception:
        logger.error("menu setup failed")
        traceback.print_exc()

    try:
        from sagittarius_maya import asset
        task = os.getenv("SAGITTARIUS_TASK", "")
        if "character" in task:
            asset.register_workspaces_for_character_model()

        elif "motion" in task:
            asset.register_workspaces_for_motion()

    except Exception:
        logger.error("task specified workspace initializer failed")
        traceback.print_exc()

    try:
        mel_cmd = """FBXProperty "Import|IncludeGrp|Geometry|OverrideNormalsLock" -v 1"""
        mel.eval(mel_cmd)
    except Exception:
        logger.error(mel_cmd)
        traceback.print_exc()

    try:
        import sagittarius_maya.asset as a
        a.register_custom_step_directories()
        a.register_character_scripts_files()
    except Exception as e:
        logger.error(e)
        traceback.print_exc()


    logger.info("sagittarius startup setup done")
    SAGITTARIUS_STARTUP_FINISHED = True
