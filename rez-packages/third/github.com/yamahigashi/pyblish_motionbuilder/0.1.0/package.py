# -*- coding: utf-8 -*-

name = 'pyblish_motionbuilder'
version = '0.1.0'
requires = [
    'pyblish_base',
    'pyblish_qml',
    'motionbuilder',
]


def commands():
    global env
    global this
    global expandvars

    if not defined("PYTHONPATH"):
        env.PYTHONPATH = "{root}/pyblish-motionbuilder"

    if defined("PYTHONPATH"):
        env.PYTHONPATH.append("{root}/pyblish-motionbuilder")
