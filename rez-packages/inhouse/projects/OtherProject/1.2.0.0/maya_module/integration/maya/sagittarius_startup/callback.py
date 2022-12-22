# -*- coding: utf-8 -*-
# pyright: reportGeneralTypeIssues=true

from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
# =============================================================================
import os
import sys
from functools import partial, update_wrapper
import traceback
# from collections import OrderedDict
from logging import getLogger, WARN, DEBUG, INFO, StreamHandler  # NOQA

from maya.api import OpenMaya as om
from maya import cmds

import gml_maya.callback as callback
import gml_maya.pathfinder as pathfinder
import sagittarius_maya.asset as asset
# ----------------------------------------------------------------------------
if sys.version_info >= (3, 0):  # pylint: disable=using-constant-test
    # For type annotation
    from typing import (  # NOQA: F401 pylint: disable=unused-import
        Optional,
        Dict,
        List,
        Tuple,
        Pattern,
        Callable,
        Any,
        Text,
        Generator,
        Union
    )
    from types import (  # NOQA: F401 pylint: disable=unused-import
        ModuleType,
    )


handler = StreamHandler()
handler.setLevel(DEBUG)

logger = getLogger(__name__)
logger.setLevel(WARN)
logger.setLevel(DEBUG)
logger.setLevel(INFO)
logger.addHandler(handler)
logger.propagate = False
# =============================================================================


CONFIG_MENU_ENTRY_POINT = "sagittarius_cofig_menu"


def generate_option_for_filenode(file):
    # type: (om.MFileObject) -> pathfinder.FinderOption
    """Genarate path finding option for this project."""

    # directory_for_search = []

    if file:
        base_dir = os.path.dirname(file.getResolvedFullName(file.rawFullName()))
    else:
        base_dir = None

    return generate_option_for_filepath(base_dir)


__option_cache = dict()


def get_cache(k):
    global __option_cache
    return __option_cache.get(k)


def set_cache(k, v):
    global __option_cache
    __option_cache[k] = v


def generate_option_for_filepath(file_path):
    # type: (Optional[Text]) -> pathfinder.FinderOption
    """Genarate path finding option for this project."""

    import gml_maya.asset as asset_util
    directory_for_search = []

    base_dir = ""
    if file_path is not None:
        if os.path.isdir(file_path):
            base_dir = file_path
        else:
            base_dir = os.path.dirname(file_path)
        base_ws = asset.search_workspace_for_given_path(base_dir)
        directory_for_search.append(base_ws)

    current_ws = cmds.workspace(q=True, fullName=True) or ""
    directory_for_search.append(current_ws)

    cache_key = current_ws + base_dir
    cache = get_cache(cache_key)
    if cache:
        return cache

    original_resources = asset.get_asset_repository_root()

    ref_model = os.path.join(original_resources, "Animation/ReferenceModel")
    if os.path.exists(ref_model):
        directory_for_search.append(ref_model)

    repo = asset.get_asset_repository_root()

    anim_ws = asset_util.list_workspaces_under_path(repo + "/Animation")
    model_ws = asset_util.list_workspaces_under_path(repo + "/Model")
    if "Animation" in current_ws:
        directory_for_search.extend(anim_ws)
        directory_for_search.extend(model_ws)

        model_ws = current_ws.replace("Animation", "Model/Body")
        directory_for_search.insert(2, model_ws)

    elif "Model" in current_ws:  
        directory_for_search.extend(model_ws)

    opt = pathfinder.FinderOption(directories=directory_for_search)
    set_cache(cache_key, opt)

    return opt


def generate_option_for_refnode(file):
    # type: (om.MFileObject) -> pathfinder.FinderOption

    import gml_maya.asset as asset_util
    repo = asset.get_asset_repository_root()
    anim_ws = asset_util.list_workspaces_under_path(repo + "/Animation")
    model_ws = asset_util.list_workspaces_under_path(repo + "/Model")

    directory_for_search = [
        cmds.workspace(q=True, fullName=True),
        repo + "/Animation/Ch000_Common"
    ]
    directory_for_search.extend(anim_ws)
    directory_for_search.extend(model_ws)

    opt = pathfinder.FinderOption(directories=directory_for_search)

    return opt


# ============================================================================
def activate_auto_repath():
    logger.info("register om.MSceneMessage.addCallback(om.MSceneMessage.kAfterOpen, auto_repath_outside_relative_path)")

    func = update_wrapper(
        partial(callback.auto_repath_file_node,
                option_generator_func=generate_option_for_filenode),
        callback.auto_repath_file_node,
    )

    callback.register(
        om.MSceneMessage.addCallback,
        om.MSceneMessage.kAfterOpen,
        func
    )

    callback.register(
        om.MSceneMessage.addCheckFileCallback,
        om.MSceneMessage.kBeforeReferenceCheck,
        func
    )

    callback.register(
        om.MSceneMessage.addCheckFileCallback,
        om.MSceneMessage.kBeforeLoadReferenceCheck,
        func
    )

    callback.register(
        om.MSceneMessage.addCallback,
        om.MSceneMessage.kAfterOpen,
        pathfinder.purge_cache
    )


def activate_auto_repath_refnode():
    logger.info("register om.MSceneMessage.addCheckFileCallback(om.MSceneMessage.kBeforeReferenceCheck, foo)")

    func = update_wrapper(
        partial(callback.auto_repath_reference_node,
                option_generator_func=generate_option_for_refnode),
        callback.auto_repath_reference_node
    )

    callback.register(
        om.MSceneMessage.addCheckFileCallback,
        om.MSceneMessage.kBeforeReferenceCheck,
        func
    )

    # om.MSceneMessage.addCheckFileCallback(
    #     om.MSceneMessage.kBeforeCreateReferenceCheck,
    #     func
    # )

    callback.register(
        om.MSceneMessage.addCheckFileCallback,
        om.MSceneMessage.kBeforeLoadReferenceCheck,
        func
    )


def activate_display_hud():
    logger.info("register om.MSceneMessage.addCheckFileCallback(om.MSceneMessage.kBeforeReferenceCheck, foo)")
    import sagittarius_maya.headupdisplay as headupdisplay

    callback.register(
        om.MSceneMessage.addCallback,
        om.MSceneMessage.kAfterOpen,
        headupdisplay.display_hud_for_current_workspace
    )


# ============================================================================
def setup():

    try:
        activate_auto_repath()
        logger.info("activate_auto_repath")
    except RuntimeError:
        traceback.print_exc()

    try:
        activate_auto_repath_refnode()
        logger.info("activate_auto_repath_refnode")
    except RuntimeError:
        traceback.print_exc()

    if cmds.about(batch=True):
        return

    else:
        setup_with_gui()


def setup_with_gui():
    try:
        callback.activate_auto_enable_vp2()
        logger.info("activate_auto_enable_vp2")
    except RuntimeError:
        traceback.print_exc()

    try:
        callback.activate_auto_60fps()
        logger.info("activate_auto_60fps")
    except RuntimeError:
        traceback.print_exc()

    try:
        callback.activate_auto_enable_colormanagement()
        logger.info("activate_auto_enable_colormanagement")
    except RuntimeError:
        traceback.print_exc()

    # try:
    #     activate_display_hud()
    #     logger.info("activate_display_hud")
    # except RuntimeError:
    #     traceback.print_exc()

    try:
        callback.register_config_menu("byk_config_menu")
    except RuntimeError:
        traceback.print_exc()
