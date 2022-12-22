# -*- coding: utf-8 -*-

name = 'pipeline'
version = '0.1.0'
requires = ['python']
tools = ["setup_project"]


def commands():
    global env
    global this
    global expandvars

    import sys
    import pathlib

    if not defined("PIPELINE_ROOT"):
        pipeline_root = pathlib.Path(sys.executable).parent.parent.parent.parent
        env.PIPELINE_ROOT = pipeline_root.as_posix()
