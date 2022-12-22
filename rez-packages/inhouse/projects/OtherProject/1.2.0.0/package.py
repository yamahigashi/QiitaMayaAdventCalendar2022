# -*- coding: utf-8 -*-

name = 'OtherProject'


@late()
def requires():
    global this
    global request
    global in_context

    requires = this._requires
    result = requires["any"][:]

    # Add request-specific requirements
    if in_context():
        for name, reqs in requires.items():
            if name not in request:
                continue

            result += reqs

    return result


def commands():
    global env
    global this
    global expandvars

    import os
    import pathlib

    def setdefault(key, value):
        if not defined(key):
            env[key] = value
        else:
            env[key] = getenv(key)

    def appenddefault(key, value):
        if not defined(key):
            env[key] = value
        else:
            env[key] = getenv(key)
            env[key].append(value)

    pipeline = env.PIPELINE_ROOT
    appenddefault("MAYA_MODULE_PATH", "{root}/maya_module")

    appenddefault("PATH", "{root}/bin")
    appenddefault("PATH", "{root}/scripts")


_requires = {
    'any': [
        'pyblish_qml',
        'pyblish_base',

        'pipeline',

        '~maya>=2018',
    ],
    'maya': [
        'mgear==4.0.9',
        'studiolibrary',
        'ymtshiftercomponents',
        'tweenmachine',
        'pyblish_maya',
    ],
    'motionbuilder': [
        'pyblish_motionbuilder',
    ]
}

