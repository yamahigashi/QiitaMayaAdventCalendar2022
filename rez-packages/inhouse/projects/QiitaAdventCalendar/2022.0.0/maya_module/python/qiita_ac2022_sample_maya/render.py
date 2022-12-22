# -*- coding: UTF-8 -*-
"""Module for playblasting"""
# ======================================================================
import re
import os
import sys
import six
import copy
import textwrap
import subprocess
from logging import getLogger

from maya import cmds
import maya.api.OpenMaya as om
import maya.api.OpenMayaUI as omui

import capture

from pathlib import Path

if sys.version_info >= (3, 0):
    # For type annotation
    from typing import (  # NOQA: F401 pylint: disable=unused-import
        TYPE_CHECKING,
    )

    if TYPE_CHECKING:
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
            Match,
            Union,
        )

logger = getLogger(__name__)
RESOLUTION_HEIGHT = 720
RESOLUTION_WIDTH = 1280

# ============================================================================================================================
# Functions


def get_render_path(directory=None):
    # type: (Optional[Text]) -> Text

    if not directory:
        directory = cmds.workspace(expandName="render")

    if not isinstance(directory, six.string_types):
        raise Exception("can not expandName render on cmds.workspace")

    if not Path(directory).exists():
        os.makedirs(directory)

    file_path = cmds.file(sn=True, q=True)
    if not file_path:
        raise Exception("can not identify scene name.")

    fname = Path(file_path).stem

    return Path(directory).joinpath(fname + ".avi").as_posix()


def render_shot(resolution=None, open_folder=True, directory=None):
    # type: (Optional[Tuple[int, int]], bool, Optional[Text]) -> None

    setting = store_camera_setting()
    start = cmds.playbackOptions(query=True, minTime=True)
    end = cmds.playbackOptions(query=True, maxTime=True)
    if not isinstance(start, float) or not isinstance(end, float):
        raise Exception("could not get minTime or maxTime by cmds.playbackOptions")

    # set_camera()
    avi = get_render_path(directory)
    mp4 = avi.replace("avi", "mp4")

    playblast(start, end, avi, resolution)
    convert(avi, mp4)

    restore_camera_setting(setting)

    # print(type(mp4))
    if open_folder:
        directory = cmds.workspace(expandName="render")
        if isinstance(directory, six.string_types):
            os.system(r"explorer {}".format(directory.replace("/", os.sep)))


def convert(in_file, out_file):
    # type: (Text, Text) -> None
    cmd = '''ffmpeg -y -i "{}" -vf format=yuv420p -c:v libx264 -r 60 "{}"'''.format(in_file, out_file)
    subprocess.call(cmd, shell=True)

    try:
        os.remove(in_file)
    except:  # noqa  # pylint: disable=bare-except
        logger.error("could not delete intermidiate avi file: %s", in_file)


def set_camera(shot, info):
    # type: (Dict[Text, Text], Dict[Text, Text]) -> None
    """Set camera parameter by given info."""
    seq = info.get("sequence_number")
    match = re.search(r"c\d+", shot.get("code", ""))

    if not match:
        return

    cut = match.group(0)
    object_mask = omui.M3dView.kDisplayTextures + omui.M3dView.kDisplayMeshes + omui.M3dView.kDisplayGrid

    cameras = cmds.ls(typ="camera") or []
    for cam in cameras:
        cam_trans = cam.replace("Shape", "")
        if seq and seq in cam_trans and cut and cut in cam_trans:
            av = omui.M3dView.active3dView()
            av.setCamera(dag_path(cam))
            av.setObjectDisplay(object_mask)
            break

    else:
        print("error")


def store_camera_setting():
    # type: () -> int
    av = omui.M3dView.active3dView()
    object_mask = av.objectDisplay()
    return object_mask


def restore_camera_setting(mask):
    # type: (int) -> None
    av = omui.M3dView.active3dView()
    av.setObjectDisplay(mask)
    av.refresh()


def dag_path(name):
    # type: (Text) -> om.MDagPath
    selectionList = om.MSelectionList()
    try:
        selectionList.add(name)
    except:
        return None

    return selectionList.getDagPath(0)


def playblast(start, end, out_file, resolution=None):
    # type: (Union[int, float], Union[int, float], Text, Optional[Tuple[int, int]]) -> None
    # selectionList = om.MSelectionList()

    if resolution is not None:
        width = resolution[0]
        height = resolution[1]

    else:
        width = RESOLUTION_WIDTH
        height = RESOLUTION_HEIGHT

    cmds.playblast(
        startTime=start,
        endTime=end,
        format="movie",
        width=width,
        height=height,
        offScreen=True,
        forceOverwrite=True,
        filename=out_file,
        percent=100,
        # compression="IYUV codec",
        viewer=False,
    )


def capture_4screens(cameras=None, directory=None, **kwargs):
    # type: (Optional[List[Text]], Optional[Text], Optional[Dict[Text, Any]]) -> None

    start = cmds.playbackOptions(query=True, minTime=True)
    end = cmds.playbackOptions(query=True, maxTime=True)
    if not isinstance(start, float) or not isinstance(end, float):
        raise Exception("could not get minTime or maxTime by cmds.playbackOptions")

    if not kwargs.get("viewport_options"):
        kwargs["viewport_options"] = {"grid": True}

    videos = []

    if not cameras:
        cameras = ["persp", "top", "front", "side"]

    options = {
        "width": None,
        "height": None,
        # "filename": avi_name,
        "start_frame": start,
        "end_frame": end,
        "frame": None,
        "format": "movie",
        # compression": 'H.264',
        "compression": "none",
        "quality": 100,
        "off_screen": False,
        "viewer": False,
        "show_ornaments": True,
        "sound": None,
        "isolate": None,
        "maintain_aspect_ratio": False,
        "overwrite": True,
        "frame_padding": 4,
        "raw_frame_numbers": False,
        "camera_options": None,
        "display_options": None,
        "viewport_options": None,
        "viewport2_options": None,
        "complete_filename": None,
    }

    options.update(**kwargs)

    for i in range(4):
        # view = omui.M3dView.get3dView(i)
        # cam = view.getCamera()
        cam = cameras[i]
        avi_name = get_render_path(directory=directory).replace(".avi", "{}.avi".format(str(i)))

        options.update({"camera": cam, "filename": avi_name})
        videos.append(avi_name.replace("/", os.sep))

        capture.capture(**options)

    width = kwargs.get("width", None)
    height = kwargs.get("height", None)

    concat_videos(
        videos,
        get_render_path(directory=directory).replace("avi", "mp4"),
        width=width,
        height=height,
        remove_src_files=True,
    )

    if True:  # open_folder:
        directory = cmds.workspace(expandName="render")
        if isinstance(directory, six.string_types):
            os.system(r"explorer {}".format(directory.replace("/", os.sep)))


def concat_videos(videos, output_path, width=None, height=None, remove_src_files=False):
    # type: (Tuple[Text, Text, Text, Text], Text, Optional[int], Optional[int], bool) -> Text

    # cmd = '''ffmpeg -y -i "{}" -vf format=yuv420p -c:v libx264 -r 60 "{}"'''.format(in_file, out_file)
    input0 = videos[0]
    input1 = videos[1]
    input2 = videos[2]
    input3 = videos[3]

    width = width or cmds.getAttr("defaultResolution.width")
    height = height or cmds.getAttr("defaultResolution.height")
    cut_w = width / 2
    cut_h = height / 2

    tmp = os.path.join(os.path.dirname(output_path), "tmp.mp4")

    cmd = textwrap.dedent(
        "ffmpeg -y -i {input0} -i {input1} -i {input2} -i {input3} "
        "-filter_complex"
        ' "'
        "[0:v][1:v][2:v][3:v]xstack=inputs=4:layout=0_0|w0_0|0_h0|w0_h0[v]"
        '" '
        '-map "[v]" '
        "-c:v libx264 -r 60 "
        "-acodec copy "
        "{tmp}".format(**locals())
    )
    subprocess.call(cmd, shell=False)

    cmd = '''ffmpeg -y -i "{}" -vf format=yuv420p -c:v libx264 -r 60 "{}"'''.format(tmp, output_path)
    subprocess.call(cmd, shell=False)

    if remove_src_files:
        try:
            for in_file in videos:
                os.remove(in_file)
            os.remove(tmp)
        except:  # noqa  # pylint: disable=bare-except
            logger.error("could not delete intermidiate avi file: %s", videos)

    return output_path


if __name__ == "__main__":
    # render_shot()
    capture_4screens()
