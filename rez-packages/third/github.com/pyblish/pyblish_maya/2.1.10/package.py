# -*- coding: utf-8 -*-

name = 'pyblish_maya'

def commands():
    global env
    global this
    global expandvars

    import pathlib
    
    if not defined("PYTHONPATH"):
        env.PYTHONPATH = "{root}/pyblish-maya-2.1.10"
    else:
        env.PYTHONPATH.append("{root}/pyblish-maya-2.1.10")


requires = [
    'pyblish_base',
    'pyblish_qml',
    'maya',
]
