# -*- coding: utf-8 -*-

name = 'python'

version = '3.8.0'

tools = ['python']

variants = [
    ['platform-windows', 'arch-AMD64', 'os-windows-10']
]

def commands():
    global env
    import pathlib
    env.PATH.prepend("{root}/../../../../../../../../bin/python/win")
