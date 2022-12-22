# -*- coding: utf-8 -*-

name = 'pyblish_qml'

def commands():
    global env
    global this
    global expandvars
    
    if not defined("PYTHONPATH"):
        env.PYTHONPATH = "{root}/pyblish-qml-1.11.4"
    else:
        env.PYTHONPATH.append("{root}/pyblish-qml-1.11.4")


requires = [
    'pyblish_base',
]
