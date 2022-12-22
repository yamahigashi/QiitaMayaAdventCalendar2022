# -*- coding: utf-8 -*-

name = 'xNormal'
version = '3.19.3'
tools = ['xnormal']
requires = []
private_build_requires = ['rezutil-1']

def commands():
    global this
    global env
    global alias
    global system

    xnormal_version = str(env.REZ_XNORMAL_VERSION)
    
    exes = ["xnormal"]
    ext = ""
    if not defined("XNORMAL_LOCATION"):
        if system.platform == "windows":
            env.XNORMAL_LOCATION = "C:/Program Files/xNormal/{}/x64/xNormal".format(str(env.REZ_XNORMAL_VERSION)).replace(" ","` ")
            ext = ".exe"
        else:
            stop("Unknown host '{}'".format(system.platform))
    
    if defined("XNORMAL_LOCATION"):
        env.PATH.append("{env.XNORMAL_LOCATION}")
    
    alias("xnormal", "{env.XNORMAL_LOCATION}" + ext)


_data = \
    {'color': '#251',
     'icon': '{root}/resources/xNormal_1.ico',
     'label': 'xNormal'}
