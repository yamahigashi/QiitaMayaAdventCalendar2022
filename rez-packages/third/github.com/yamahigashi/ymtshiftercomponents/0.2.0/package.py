# -*- coding: utf-8 -*-

name = 'ymtshiftercomponents'
version = '0.2.0'
requires = ['~maya-2015+<3000']


def commands():
    global env
    global this
    global expandvars

    if not defined("MAYA_MODULE_PATH"):
        env.MAYA_MODULE_PATH = "{root}/mgear_shifter_components"

    if defined("MAYA_MODULE_PATH"):
        env.MAYA_MODULE_PATH.append("{root}/mgear_shifter_components")
