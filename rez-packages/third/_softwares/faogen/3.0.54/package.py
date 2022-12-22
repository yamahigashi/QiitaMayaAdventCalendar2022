# -*- coding: utf-8 -*-
name = 'faogen'
version = '3.0.54'
tools = ['faogen']
requires = []

def commands():
    global this
    global env
    global alias
    global system

    xnormal_version = str(env.REZ_FAOGEN_VERSION)
    
    exes = ["faogen"]
    ext = ""
    if not defined("FAOGEN_LOCATION"):
        if system.platform == "windows":
            env.FAOGEN_LOCATION = "C:/Program Files/Faogen 3/faogen".replace(" ","` ")
            ext = ".exe"
        else:
            stop("Unknown host '{}'".format(system.platform))
    
    if defined("FAOGEN_LOCATION"):
        env.PATH.append("{env.FAOGEN_LOCATION}")
    
    alias("faogen", "{env.FAOGEN_LOCATION}" + ext)


_data = \
    {'color': '#251',
     'icon': '{root}/resources/faogen_101.ico',
     'label': 'Faogen'}
