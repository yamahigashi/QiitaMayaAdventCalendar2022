# -*- coding: utf-8 -*-
import textwrap
import maya.cmds as cmds


MENU_NAME = "qiita_ac_2022"
MENU_LABEL = "QiitaAC2022"


def register():

    if cmds.menu(MENU_NAME, exists=True):
        cmds.deleteUI(MENU_NAME)

    # the top menu
    cmds.menu(
        MENU_NAME,
        label=MENU_LABEL,
        parent='MayaWindow',
        tearOff=True,
        allowOptionBoxes=True
    )

    # ------------------------------------------------------------------------
    cmds.menuItem(
        parent=MENU_NAME,
        label="Render 4Screens",
        echoCommand=True,
        command=textwrap.dedent(
            '''
                import qiita_ac2022_sample_maya.render as r
                r.capture_4screens()
            ''')
    )


    # ------------------------------------------------------------------------
