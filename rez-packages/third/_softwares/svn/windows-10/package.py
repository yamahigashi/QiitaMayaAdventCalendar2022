# -*- coding: utf-8 -*-

name = 'svn'
version = 'windows-10'

requires = [
    'platform-windows',
    'arch-AMD64'
]


def commands():
    global env
    env["PATH"].prepend("{root}/bin")
