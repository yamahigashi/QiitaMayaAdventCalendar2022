# -*- coding: utf-8 -*-

name = 'studiolibrary'

version = '2.7.1'

requires = ['~maya-2015+<3000']

private_build_requires = ['rezutil-1']

def commands():
    global env
    global this
    global expandvars
    
    if not defined("MAYA_MODULE_PATH"):
        env.MAYA_MODULE_PATH = "{root}"
    
    if defined("MAYA_MODULE_PATH"):
        env.MAYA_MODULE_PATH.append("{root}")
