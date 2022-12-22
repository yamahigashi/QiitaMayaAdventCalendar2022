# -*- coding: utf-8 -*-

name = 'rezutil'

version = '1.3.2'

requires = ['python']

def commands():
    global env
    env["PYTHONPATH"].prepend("{root}/python")
