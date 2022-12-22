# -*- coding: utf-8 -*-

name = 'FBXPythonSDK'

variants = [

    ['platform-windows', 'python-3.9'],
    ['platform-windows', 'python-3.7'],
]


def commands():
    global env
    global this
    global expandvars
    import platform

    if not defined("PYTHONPATH"):
        env.PYTHONPATH = "{root}/lib"
    else:
        env.PYTHONPATH.append("{root}/lib")
