# -*- coding: utf-8 -*-

name = "motionbuilder"
version = "2023"
build_command = False

description = \
"""
Autodesk MotionBuilder
"""

tools = [
    "motionbuilder",
    "mayapy"
]

def commands():
    global env
    import platform
    
    platform_name = platform.system().lower()
    
    env["MOTIONBUILDER_VERSION"] = "2023"
    
    if platform_name == "windows":
        env["MOTIONBUILDER_LOCATION"] = "C:/Program Files/Autodesk/MotionBuilder {env.MOTIONBUILDER_VERSION}"

        env["PATH"].append("C:/Program Files/Common Files/Autodesk Shared/")
        env["PATH"].append("C:/Program Files (x86)/Autodesk/Backburner/")
        
    elif platform_name == "linux":
        env["MOTIONBUILDER_LOCATION"] = "/usr/autodesk/maya{env.MOTIONBUILDER_VERSION}"
        
    elif platform_name == "darwin":
        env["MOTIONBUILDER_LOCATION"] = "/Applications/Autodesk/maya{env.MOTIONBUILDER_VERSION}/Maya.app/Contents"
        env["DYLD_LIBRARY_PATH"] = "{env.MOTIONBUILDER_LOCATION}/MacOS"
        
    env["PATH"].append("{env.MOTIONBUILDER_LOCATION}/bin/x64")

    # Override some Maya default settings (optimization)
    # todo: These might need to be moved out to be left to company specific choices
    env["MOTIONBUILDER_DISABLE_CLIC_IPM"] = "Yes"
    env["MOTIONBUILDER_DISABLE_CIP"] = "Yes"
    env["MOTIONBUILDER_DISABLE_CER"] = "Yes"
    env["PYMEL_SKIP_MEL_INIT"] = "Yes"
    env["LC_ALL"] = "C"
    # env["MOTIONBUILDER_PYTHON_VERSION"] = "2"
    
    env.MOTIONBUILDER_VERSION = this.version
    # env.MOTIONBUILDER_UI_LANGUAGE = "en_US"
    env.MOTIONBUILDER_DISABLE_CIP = "1"

_data = \
    {'color': '#251',
     'icon': '{root}/resources/maya-2023-badge-75x75.png',
     'label': 'Autodesk MotionBuilder'}
