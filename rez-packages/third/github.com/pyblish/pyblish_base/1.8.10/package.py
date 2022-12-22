# -*- coding: utf-8 -*-

name = 'pyblish_base'

def commands():
    global env
    global this
    global expandvars

    import pathlib

    if not defined("PYTHONPATH"):
        env.PYTHONPATH = "{root}/pyblish-base-1.8.10"
    else:
        env.PYTHONPATH.append("{root}/pyblish-base-1.8.10")

    if not defined("PYBLISH_QML_PYTHON_EXECUTABLE"):
        pipeline = env.PIPELINE_ROOT
        env.PYBLISH_QML_PYTHON_EXECUTABLE = pathlib.Path(pipeline.value()).joinpath("bin/python-3.9/win/python.exe").as_posix()

requires = [
    'pipeline',
]
