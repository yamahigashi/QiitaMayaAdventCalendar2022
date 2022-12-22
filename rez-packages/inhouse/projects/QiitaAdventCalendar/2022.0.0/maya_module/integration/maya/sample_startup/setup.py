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


STARTUP_FINISHED = False

###############################################################################


def setup():

    global STARTUP_FINISHED

    import maya.cmds as cmds
    import maya.mel as mel

    logger.info("sample startup setup start")

    if STARTUP_FINISHED:
        return

    try:
        from . import plugins
        plugins.setup()

    except Exception:
        logger.error("plugins setup failed")
        traceback.print_exc()

    try:
        if not cmds.about(batch=True):
            from qiita_ac2022_sample_maya import menu
            menu.register()

    except Exception:
        logger.error("menu setup failed")
        traceback.print_exc()

    try:
        mel_cmd = """FBXProperty "Import|IncludeGrp|Geometry|OverrideNormalsLock" -v 1"""
        mel.eval(mel_cmd)
    except Exception:
        logger.error(mel_cmd)
        traceback.print_exc()

    logger.info("sample startup setup done")
    STARTUP_FINISHED = True
