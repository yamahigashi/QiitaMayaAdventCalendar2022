# -*- coding: utf-8 -*-

name = "maya"
version = "2017"
build_command = False
variants = [
    ["maya_ui_language-2.en_US"],
    ["maya_ui_language-1.ja_JP"],
    ["maya_ui_language-0.zh_CN"],
]
requires = ['python-2.7']

description = \
"""
Autodesk Maya
"""

tools = [
    "maya",
    "mayapy"
]

def commands():
    global env
    import platform
    
    platform_name = platform.system().lower()
    
    env["MAYA_VERSION"] = "2017"
    
    if platform_name == "windows":
        env["MAYA_LOCATION"] = "C:/Program Files/Autodesk/Maya{env.MAYA_VERSION}"
        
        env["PATH"].append("C:/Program Files/Common Files/Autodesk Shared/")
        env["PATH"].append("C:/Program Files (x86)/Autodesk/Backburner/")
        
    elif platform_name == "linux":
        env["MAYA_LOCATION"] = "/usr/autodesk/maya{env.MAYA_VERSION}"
        
    elif platform_name == "darwin":
        env["MAYA_LOCATION"] = "/Applications/Autodesk/maya{env.MAYA_VERSION}/Maya.app/Contents"
        env["DYLD_LIBRARY_PATH"] = "{env.MAYA_LOCATION}/MacOS"
        
    env["PATH"].append("{env.MAYA_LOCATION}/bin")

    # Override some Maya default settings (optimization)
    # todo: These might need to be moved out to be left to company specific choices
    env["MAYA_DISABLE_CLIC_IPM"] = "Yes"
    env["MAYA_DISABLE_CIP"] = "Yes"
    env["MAYA_DISABLE_CER"] = "Yes"
    env["PYMEL_SKIP_MEL_INIT"] = "Yes"
    env["LC_ALL"] = "C"
    
    env.MAYA_VERSION = this.version
    # env.MAYA_UI_LANGUAGE = "en_US"
    env.MAYA_DISABLE_CIP = "1"

_data = \
    {'color': '#251',
     'icon': '{root}/resources/icon_256x256.png',
     'label': 'Autodesk Maya'}
