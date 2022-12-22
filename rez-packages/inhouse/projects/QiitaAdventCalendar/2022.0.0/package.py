# -*- coding: utf-8 -*-

name = 'AdventCalendar'


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
    setdefault("ADVENTCALENDAR_SAMPLE_PROJECT_ROOT", pathlib.Path(pipeline.value()).parent.joinpath("sample").as_posix())
    setdefault("ADVENTCALENDAR_SAMPLE_RESOURCE_REPOSITORY_ROOT", pathlib.Path(pipeline.value()).parent.joinpath("sample").as_posix())
    setdefault("ADVENTCALENDAR_SHARED_DRIVE_LETTER", "R")
    setdefault("MOTIONBUILDER_PYTHON_STARTUP", "{root}/mobu_module/integration/mobu")

    appenddefault("PYTHONPATH", "{root}/python")
    appenddefault("PYTHONPATH", "{root}/mobu_module/python")
    appenddefault("PYTHONPATH", "{root}/mobu_module/mbscripts")
    appenddefault("PYTHONPATH", "{root}/mobu_module/vendor_python")

    appenddefault("PATH", "{root}/bin")
    appenddefault("PATH", "{root}/scripts")


_requires = {
    'any': [
        'pyblish_qml',
        'pyblish_base',
        'ffmpeg',
        'pipeline',

        '~maya>=2020',
        '~motionbuilder>=2020',
        '~xnormal',
        '~faogen',
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


_data = {
    'color': '#251',
    'icon': '{root}/resources/qiita.png',
    'label': 'QiitaAdventCalendar'
}
