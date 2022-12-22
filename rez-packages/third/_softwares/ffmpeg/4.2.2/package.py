# -*- coding: utf-8 -*-

name = 'ffmpeg'
version = '4.2.2'

requires = [
    'platform-windows',
    'arch-AMD64'
]


def commands():
    global env
    env["PATH"].prepend("{root}/bin")
