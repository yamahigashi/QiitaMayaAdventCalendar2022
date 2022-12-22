# -*- coding: utf-8 -*-

name = 'mgear'

requires = ['~maya-2015+<3000']

private_build_requires = ['rezutil-1']

def commands():
    global env
    global this
    global expandvars

    if not defined("MAYA_MODULE_PATH"):
        env.MAYA_MODULE_PATH = "{root}/release"

    if defined("MAYA_MODULE_PATH"):
        env.MAYA_MODULE_PATH.append("{root}/release")
