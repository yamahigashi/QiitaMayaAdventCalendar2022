# -*- coding: utf-8 -*-

name = 'tweenmachine'
version = '3.1.0'
requires = ['~maya-2015+<3000']


def commands():
    global env
    global this
    global expandvars

    if not defined("MAYA_PLUG_IN_PATH"):
        env.MAYA_PLUG_IN_PATH = "{root}/tweenMachine/python"

    if defined("MAYA_PLUG_IN_PATH"):
        env.MAYA_PLUG_IN_PATH.append("{root}/tweenMachine/python")
