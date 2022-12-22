# # -*- coding: utf-8 -*-
import maya.cmds as cmds


def __register_main_menu():
    from textwrap import dedent
    cmds.evalDeferred(dedent(
        """
        import sagittarius_startup.setup as s

        s.setup()
        """
    ))


if __name__ == '__main__':
    try:
        __register_main_menu()

    except Exception:
        # avoidng the "call userSetup.py chain" accidentally stop, all exception must collapse
        import traceback
        traceback.print_exc()
