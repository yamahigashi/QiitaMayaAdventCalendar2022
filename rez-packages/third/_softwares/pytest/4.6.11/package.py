# -*- coding: utf-8 -*-

name = "pytest"
version = '4.6.11'
build_command = False

def commands():
    global env
    env["PYTHONPATH"].append("{root}/site-packages")
    env["PATH"].append("{root}/bin")
