# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/matsumoto/projects/gdl/svn/trunk/maya/maya_modules/red/python/gml_component/gml_control_01/settingsUI.ui'
#
# Created: Wed Feb 22 19:58:13 2017
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(280, 901)
        self.ikRefArray_groupBox = QtWidgets.QGroupBox(Form)
        self.ikRefArray_groupBox.setGeometry(QtCore.QRect(10, 430, 249, 175))
        self.ikRefArray_groupBox.setObjectName("ikRefArray_groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.ikRefArray_groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 231, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.ikRefArray_horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.ikRefArray_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.ikRefArray_horizontalLayout.setObjectName("ikRefArray_horizontalLayout")
        self.ikRefArray_verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.ikRefArray_verticalLayout_1.setObjectName("ikRefArray_verticalLayout_1")
        self.ikRefArray_listWidget = QtWidgets.QListWidget(self.layoutWidget)
        self.ikRefArray_listWidget.setDragDropOverwriteMode(True)
        self.ikRefArray_listWidget.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.ikRefArray_listWidget.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.ikRefArray_listWidget.setAlternatingRowColors(True)
        self.ikRefArray_listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.ikRefArray_listWidget.setSelectionRectVisible(False)
        self.ikRefArray_listWidget.setObjectName("ikRefArray_listWidget")
        self.ikRefArray_verticalLayout_1.addWidget(self.ikRefArray_listWidget)
        self.ikRefArray_horizontalLayout.addLayout(self.ikRefArray_verticalLayout_1)
        self.ikRefArray_verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.ikRefArray_verticalLayout_2.setObjectName("ikRefArray_verticalLayout_2")
        self.ikRefArrayAdd_pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.ikRefArrayAdd_pushButton.setObjectName("ikRefArrayAdd_pushButton")
        self.ikRefArray_verticalLayout_2.addWidget(self.ikRefArrayAdd_pushButton)
        self.ikRefArrayRemove_pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.ikRefArrayRemove_pushButton.setObjectName("ikRefArrayRemove_pushButton")
        self.ikRefArray_verticalLayout_2.addWidget(self.ikRefArrayRemove_pushButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.ikRefArray_verticalLayout_2.addItem(spacerItem)
        self.ikRefArray_horizontalLayout.addLayout(self.ikRefArray_verticalLayout_2)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(1, 9, 249, 221))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 10, 221, 202))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.joint_checkBox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.joint_checkBox.setObjectName("joint_checkBox")
        self.verticalLayout_4.addWidget(self.joint_checkBox)
        self.uniScale_checkBox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.uniScale_checkBox.setObjectName("uniScale_checkBox")
        self.verticalLayout_4.addWidget(self.uniScale_checkBox)
        self.neutralRotation_checkBox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.neutralRotation_checkBox.setObjectName("neutralRotation_checkBox")
        self.verticalLayout_4.addWidget(self.neutralRotation_checkBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.controlShape_label = QtWidgets.QLabel(self.layoutWidget1)
        self.controlShape_label.setText("Control Shape")
        self.controlShape_label.setObjectName("controlShape_label")
        self.horizontalLayout_2.addWidget(self.controlShape_label)
        self.controlShape_comboBox = QtWidgets.QComboBox(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.controlShape_comboBox.sizePolicy().hasHeightForWidth())
        self.controlShape_comboBox.setSizePolicy(sizePolicy)
        self.controlShape_comboBox.setObjectName("controlShape_comboBox")
        self.controlShape_comboBox.addItem("")
        self.controlShape_comboBox.addItem("")
        self.controlShape_comboBox.addItem("")
        self.controlShape_comboBox.addItem("")
        self.controlShape_comboBox.addItem("")
        self.controlShape_comboBox.addItem("")
        self.controlShape_comboBox.addItem("")
        self.controlShape_comboBox.addItem("")
        self.controlShape_comboBox.addItem("")
        self.controlShape_comboBox.addItem("")
        self.controlShape_comboBox.addItem("")
        self.controlShape_comboBox.addItem("")
        self.controlShape_comboBox.addItem("")
        self.controlShape_comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.controlShape_comboBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ctlSize_label = QtWidgets.QLabel(self.layoutWidget1)
        self.ctlSize_label.setObjectName("ctlSize_label")
        self.horizontalLayout_3.addWidget(self.ctlSize_label)
        self.ctlSize_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ctlSize_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.ctlSize_doubleSpinBox.setSizePolicy(sizePolicy)
        self.ctlSize_doubleSpinBox.setWrapping(False)
        self.ctlSize_doubleSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.ctlSize_doubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.ctlSize_doubleSpinBox.setMinimum(0.01)
        self.ctlSize_doubleSpinBox.setMaximum(200.0)
        self.ctlSize_doubleSpinBox.setProperty("value", 1.0)
        self.ctlSize_doubleSpinBox.setObjectName("ctlSize_doubleSpinBox")
        self.horizontalLayout_3.addWidget(self.ctlSize_doubleSpinBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.ctlOffsetScl_label = QtWidgets.QLabel(self.layoutWidget1)
        self.ctlOffsetScl_label.setObjectName("ctlOffsetScl_label")
        self.horizontalLayout_6.addWidget(self.ctlOffsetScl_label)
        self.ctlOffsetSclX_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ctlOffsetSclX_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.ctlOffsetSclX_doubleSpinBox.setSizePolicy(sizePolicy)
        self.ctlOffsetSclX_doubleSpinBox.setWrapping(False)
        self.ctlOffsetSclX_doubleSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.ctlOffsetSclX_doubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.ctlOffsetSclX_doubleSpinBox.setMinimum(-360.0)
        self.ctlOffsetSclX_doubleSpinBox.setMaximum(360.0)
        self.ctlOffsetSclX_doubleSpinBox.setSingleStep(1.0)
        self.ctlOffsetSclX_doubleSpinBox.setProperty("value", 0.0)
        self.ctlOffsetSclX_doubleSpinBox.setObjectName("ctlOffsetSclX_doubleSpinBox")
        self.horizontalLayout_6.addWidget(self.ctlOffsetSclX_doubleSpinBox)
        self.ctlOffsetSclY_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ctlOffsetSclY_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.ctlOffsetSclY_doubleSpinBox.setSizePolicy(sizePolicy)
        self.ctlOffsetSclY_doubleSpinBox.setWrapping(False)
        self.ctlOffsetSclY_doubleSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.ctlOffsetSclY_doubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.ctlOffsetSclY_doubleSpinBox.setMinimum(-360.0)
        self.ctlOffsetSclY_doubleSpinBox.setMaximum(360.0)
        self.ctlOffsetSclY_doubleSpinBox.setProperty("value", 0.0)
        self.ctlOffsetSclY_doubleSpinBox.setObjectName("ctlOffsetSclY_doubleSpinBox")
        self.horizontalLayout_6.addWidget(self.ctlOffsetSclY_doubleSpinBox)
        self.ctlOffsetSclZ_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ctlOffsetSclZ_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.ctlOffsetSclZ_doubleSpinBox.setSizePolicy(sizePolicy)
        self.ctlOffsetSclZ_doubleSpinBox.setWrapping(False)
        self.ctlOffsetSclZ_doubleSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.ctlOffsetSclZ_doubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.ctlOffsetSclZ_doubleSpinBox.setMinimum(-360.0)
        self.ctlOffsetSclZ_doubleSpinBox.setMaximum(360.0)
        self.ctlOffsetSclZ_doubleSpinBox.setProperty("value", 0.0)
        self.ctlOffsetSclZ_doubleSpinBox.setObjectName("ctlOffsetSclZ_doubleSpinBox")
        self.horizontalLayout_6.addWidget(self.ctlOffsetSclZ_doubleSpinBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.ctlOffsetRot_label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.ctlOffsetRot_label_2.setObjectName("ctlOffsetRot_label_2")
        self.horizontalLayout_5.addWidget(self.ctlOffsetRot_label_2)
        self.ctlOffsetRotX_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ctlOffsetRotX_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.ctlOffsetRotX_doubleSpinBox.setSizePolicy(sizePolicy)
        self.ctlOffsetRotX_doubleSpinBox.setWrapping(False)
        self.ctlOffsetRotX_doubleSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.ctlOffsetRotX_doubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.ctlOffsetRotX_doubleSpinBox.setMinimum(-360.0)
        self.ctlOffsetRotX_doubleSpinBox.setMaximum(360.0)
        self.ctlOffsetRotX_doubleSpinBox.setSingleStep(1.0)
        self.ctlOffsetRotX_doubleSpinBox.setProperty("value", 0.0)
        self.ctlOffsetRotX_doubleSpinBox.setObjectName("ctlOffsetRotX_doubleSpinBox")
        self.horizontalLayout_5.addWidget(self.ctlOffsetRotX_doubleSpinBox)
        self.ctlOffsetRotY_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ctlOffsetRotY_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.ctlOffsetRotY_doubleSpinBox.setSizePolicy(sizePolicy)
        self.ctlOffsetRotY_doubleSpinBox.setWrapping(False)
        self.ctlOffsetRotY_doubleSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.ctlOffsetRotY_doubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.ctlOffsetRotY_doubleSpinBox.setMinimum(-360.0)
        self.ctlOffsetRotY_doubleSpinBox.setMaximum(360.0)
        self.ctlOffsetRotY_doubleSpinBox.setProperty("value", 0.0)
        self.ctlOffsetRotY_doubleSpinBox.setObjectName("ctlOffsetRotY_doubleSpinBox")
        self.horizontalLayout_5.addWidget(self.ctlOffsetRotY_doubleSpinBox)
        self.ctlOffsetRotZ_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ctlOffsetRotZ_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.ctlOffsetRotZ_doubleSpinBox.setSizePolicy(sizePolicy)
        self.ctlOffsetRotZ_doubleSpinBox.setWrapping(False)
        self.ctlOffsetRotZ_doubleSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.ctlOffsetRotZ_doubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.ctlOffsetRotZ_doubleSpinBox.setMinimum(-360.0)
        self.ctlOffsetRotZ_doubleSpinBox.setMaximum(360.0)
        self.ctlOffsetRotZ_doubleSpinBox.setProperty("value", 0.0)
        self.ctlOffsetRotZ_doubleSpinBox.setObjectName("ctlOffsetRotZ_doubleSpinBox")
        self.horizontalLayout_5.addWidget(self.ctlOffsetRotZ_doubleSpinBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ctlOffsetPos_label = QtWidgets.QLabel(self.layoutWidget1)
        self.ctlOffsetPos_label.setObjectName("ctlOffsetPos_label")
        self.horizontalLayout_4.addWidget(self.ctlOffsetPos_label)
        self.ctlOffsetPosX_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ctlOffsetPosX_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.ctlOffsetPosX_doubleSpinBox.setSizePolicy(sizePolicy)
        self.ctlOffsetPosX_doubleSpinBox.setWrapping(False)
        self.ctlOffsetPosX_doubleSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.ctlOffsetPosX_doubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.ctlOffsetPosX_doubleSpinBox.setMinimum(-999.0)
        self.ctlOffsetPosX_doubleSpinBox.setMaximum(999.0)
        self.ctlOffsetPosX_doubleSpinBox.setProperty("value", 0.0)
        self.ctlOffsetPosX_doubleSpinBox.setObjectName("ctlOffsetPosX_doubleSpinBox")
        self.horizontalLayout_4.addWidget(self.ctlOffsetPosX_doubleSpinBox)
        self.ctlOffsetPosY_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ctlOffsetPosY_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.ctlOffsetPosY_doubleSpinBox.setSizePolicy(sizePolicy)
        self.ctlOffsetPosY_doubleSpinBox.setWrapping(False)
        self.ctlOffsetPosY_doubleSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.ctlOffsetPosY_doubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.ctlOffsetPosY_doubleSpinBox.setMinimum(-999.0)
        self.ctlOffsetPosY_doubleSpinBox.setMaximum(999.0)
        self.ctlOffsetPosY_doubleSpinBox.setProperty("value", 0.0)
        self.ctlOffsetPosY_doubleSpinBox.setObjectName("ctlOffsetPosY_doubleSpinBox")
        self.horizontalLayout_4.addWidget(self.ctlOffsetPosY_doubleSpinBox)
        self.ctlOffsetPosZ_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ctlOffsetPosZ_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.ctlOffsetPosZ_doubleSpinBox.setSizePolicy(sizePolicy)
        self.ctlOffsetPosZ_doubleSpinBox.setWrapping(False)
        self.ctlOffsetPosZ_doubleSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.ctlOffsetPosZ_doubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.ctlOffsetPosZ_doubleSpinBox.setMinimum(-999.0)
        self.ctlOffsetPosZ_doubleSpinBox.setMaximum(999.0)
        self.ctlOffsetPosZ_doubleSpinBox.setProperty("value", 0.0)
        self.ctlOffsetPosZ_doubleSpinBox.setObjectName("ctlOffsetPosZ_doubleSpinBox")
        self.horizontalLayout_4.addWidget(self.ctlOffsetPosZ_doubleSpinBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.keyable_groupBox = QtWidgets.QGroupBox(Form)
        self.keyable_groupBox.setGeometry(QtCore.QRect(0, 260, 251, 171))
        self.keyable_groupBox.setObjectName("keyable_groupBox")
        self.layoutWidget2 = QtWidgets.QWidget(self.keyable_groupBox)
        self.layoutWidget2.setGeometry(QtCore.QRect(9, 16, 245, 145))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.translate_pushButton = QtWidgets.QPushButton(self.layoutWidget2)
        self.translate_pushButton.setObjectName("translate_pushButton")
        self.verticalLayout.addWidget(self.translate_pushButton)
        self.tx_checkBox = QtWidgets.QCheckBox(self.layoutWidget2)
        self.tx_checkBox.setObjectName("tx_checkBox")
        self.verticalLayout.addWidget(self.tx_checkBox)
        self.ty_checkBox = QtWidgets.QCheckBox(self.layoutWidget2)
        self.ty_checkBox.setObjectName("ty_checkBox")
        self.verticalLayout.addWidget(self.ty_checkBox)
        self.tz_checkBox = QtWidgets.QCheckBox(self.layoutWidget2)
        self.tz_checkBox.setObjectName("tz_checkBox")
        self.verticalLayout.addWidget(self.tz_checkBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.rotate_pushButton = QtWidgets.QPushButton(self.layoutWidget2)
        self.rotate_pushButton.setObjectName("rotate_pushButton")
        self.verticalLayout_2.addWidget(self.rotate_pushButton)
        self.rx_checkBox = QtWidgets.QCheckBox(self.layoutWidget2)
        self.rx_checkBox.setObjectName("rx_checkBox")
        self.verticalLayout_2.addWidget(self.rx_checkBox)
        self.ry_checkBox = QtWidgets.QCheckBox(self.layoutWidget2)
        self.ry_checkBox.setObjectName("ry_checkBox")
        self.verticalLayout_2.addWidget(self.ry_checkBox)
        self.rz_checkBox = QtWidgets.QCheckBox(self.layoutWidget2)
        self.rz_checkBox.setObjectName("rz_checkBox")
        self.verticalLayout_2.addWidget(self.rz_checkBox)
        self.ro_checkBox = QtWidgets.QCheckBox(self.layoutWidget2)
        self.ro_checkBox.setObjectName("ro_checkBox")
        self.verticalLayout_2.addWidget(self.ro_checkBox)
        self.ro_comboBox = QtWidgets.QComboBox(self.layoutWidget2)
        self.ro_comboBox.setObjectName("ro_comboBox")
        self.ro_comboBox.addItem("")
        self.ro_comboBox.addItem("")
        self.ro_comboBox.addItem("")
        self.ro_comboBox.addItem("")
        self.ro_comboBox.addItem("")
        self.ro_comboBox.addItem("")
        self.verticalLayout_2.addWidget(self.ro_comboBox)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scale_pushButton = QtWidgets.QPushButton(self.layoutWidget2)
        self.scale_pushButton.setObjectName("scale_pushButton")
        self.verticalLayout_3.addWidget(self.scale_pushButton)
        self.sx_checkBox = QtWidgets.QCheckBox(self.layoutWidget2)
        self.sx_checkBox.setObjectName("sx_checkBox")
        self.verticalLayout_3.addWidget(self.sx_checkBox)
        self.sy_checkBox = QtWidgets.QCheckBox(self.layoutWidget2)
        self.sy_checkBox.setObjectName("sy_checkBox")
        self.verticalLayout_3.addWidget(self.sy_checkBox)
        self.sz_checkBox = QtWidgets.QCheckBox(self.layoutWidget2)
        self.sz_checkBox.setObjectName("sz_checkBox")
        self.verticalLayout_3.addWidget(self.sz_checkBox)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.rotRefArray_groupBox = QtWidgets.QGroupBox(Form)
        self.rotRefArray_groupBox.setGeometry(QtCore.QRect(10, 600, 249, 175))
        self.rotRefArray_groupBox.setObjectName("rotRefArray_groupBox")
        self.layoutWidget_2 = QtWidgets.QWidget(self.rotRefArray_groupBox)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 20, 231, 141))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.rotRefArray_horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.rotRefArray_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.rotRefArray_horizontalLayout.setObjectName("rotRefArray_horizontalLayout")
        self.rotRefArray_verticalLayout = QtWidgets.QVBoxLayout()
        self.rotRefArray_verticalLayout.setObjectName("rotRefArray_verticalLayout")
        self.rotRefArray_listWidget = QtWidgets.QListWidget(self.layoutWidget_2)
        self.rotRefArray_listWidget.setDragDropOverwriteMode(True)
        self.rotRefArray_listWidget.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.rotRefArray_listWidget.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.rotRefArray_listWidget.setAlternatingRowColors(True)
        self.rotRefArray_listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.rotRefArray_listWidget.setSelectionRectVisible(False)
        self.rotRefArray_listWidget.setObjectName("rotRefArray_listWidget")
        self.rotRefArray_verticalLayout.addWidget(self.rotRefArray_listWidget)
        self.rotRefArray_horizontalLayout.addLayout(self.rotRefArray_verticalLayout)
        self.rotRefArray_verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.rotRefArray_verticalLayout_2.setObjectName("rotRefArray_verticalLayout_2")
        self.rotRefArrayAdd_pushButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.rotRefArrayAdd_pushButton.setObjectName("rotRefArrayAdd_pushButton")
        self.rotRefArray_verticalLayout_2.addWidget(self.rotRefArrayAdd_pushButton)
        self.rotRefArrayRemove_pushButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.rotRefArrayRemove_pushButton.setObjectName("rotRefArrayRemove_pushButton")
        self.rotRefArray_verticalLayout_2.addWidget(self.rotRefArrayRemove_pushButton)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.rotRefArray_verticalLayout_2.addItem(spacerItem3)
        self.rotRefArray_horizontalLayout.addLayout(self.rotRefArray_verticalLayout_2)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.translate_pushButton, QtCore.SIGNAL("clicked()"), self.tz_checkBox.toggle)
        QtCore.QObject.connect(self.translate_pushButton, QtCore.SIGNAL("clicked()"), self.ty_checkBox.toggle)
        QtCore.QObject.connect(self.translate_pushButton, QtCore.SIGNAL("clicked()"), self.tx_checkBox.toggle)
        QtCore.QObject.connect(self.rotate_pushButton, QtCore.SIGNAL("clicked()"), self.rx_checkBox.toggle)
        QtCore.QObject.connect(self.rotate_pushButton, QtCore.SIGNAL("clicked()"), self.ry_checkBox.toggle)
        QtCore.QObject.connect(self.rotate_pushButton, QtCore.SIGNAL("clicked()"), self.rz_checkBox.toggle)
        QtCore.QObject.connect(self.rotate_pushButton, QtCore.SIGNAL("clicked()"), self.ro_checkBox.toggle)
        QtCore.QObject.connect(self.scale_pushButton, QtCore.SIGNAL("clicked()"), self.sx_checkBox.toggle)
        QtCore.QObject.connect(self.scale_pushButton, QtCore.SIGNAL("clicked()"), self.sy_checkBox.toggle)
        QtCore.QObject.connect(self.scale_pushButton, QtCore.SIGNAL("clicked()"), self.sz_checkBox.toggle)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.ikRefArray_groupBox.setTitle(QtWidgets.QApplication.translate("Form", "IK Reference Array", None, -1))
        self.ikRefArrayAdd_pushButton.setText(QtWidgets.QApplication.translate("Form", "<<", None, -1))
        self.ikRefArrayRemove_pushButton.setText(QtWidgets.QApplication.translate("Form", ">>", None, -1))
        self.joint_checkBox.setText(QtWidgets.QApplication.translate("Form", "Joint", None, -1))
        self.uniScale_checkBox.setText(QtWidgets.QApplication.translate("Form", "Uniform Scale", None, -1))
        self.neutralRotation_checkBox.setText(QtWidgets.QApplication.translate("Form", "World Space Orientation Align", None, -1))
        self.controlShape_comboBox.setItemText(0, QtWidgets.QApplication.translate("Form", "Arrow", None, -1))
        self.controlShape_comboBox.setItemText(1, QtWidgets.QApplication.translate("Form", "Circle", None, -1))
        self.controlShape_comboBox.setItemText(2, QtWidgets.QApplication.translate("Form", "Compas", None, -1))
        self.controlShape_comboBox.setItemText(3, QtWidgets.QApplication.translate("Form", "Cross", None, -1))
        self.controlShape_comboBox.setItemText(4, QtWidgets.QApplication.translate("Form", "Crossarrow", None, -1))
        self.controlShape_comboBox.setItemText(5, QtWidgets.QApplication.translate("Form", "Cube", None, -1))
        self.controlShape_comboBox.setItemText(6, QtWidgets.QApplication.translate("Form", "Cubewithpeak", None, -1))
        self.controlShape_comboBox.setItemText(7, QtWidgets.QApplication.translate("Form", "Cylinder", None, -1))
        self.controlShape_comboBox.setItemText(8, QtWidgets.QApplication.translate("Form", "Diamond", None, -1))
        self.controlShape_comboBox.setItemText(9, QtWidgets.QApplication.translate("Form", "Flower", None, -1))
        self.controlShape_comboBox.setItemText(10, QtWidgets.QApplication.translate("Form", "Null", None, -1))
        self.controlShape_comboBox.setItemText(11, QtWidgets.QApplication.translate("Form", "Pyramid", None, -1))
        self.controlShape_comboBox.setItemText(12, QtWidgets.QApplication.translate("Form", "Sphere", None, -1))
        self.controlShape_comboBox.setItemText(13, QtWidgets.QApplication.translate("Form", "Square", None, -1))
        self.ctlSize_label.setText(QtWidgets.QApplication.translate("Form", "Ctl Size", None, -1))
        self.ctlOffsetScl_label.setText(QtWidgets.QApplication.translate("Form", "S Offset", None, -1))
        self.ctlOffsetRot_label_2.setText(QtWidgets.QApplication.translate("Form", "R Offset", None, -1))
        self.ctlOffsetPos_label.setText(QtWidgets.QApplication.translate("Form", "T Offset", None, -1))
        self.keyable_groupBox.setTitle(QtWidgets.QApplication.translate("Form", "Keyable", None, -1))
        self.translate_pushButton.setText(QtWidgets.QApplication.translate("Form", "Translate", None, -1))
        self.tx_checkBox.setText(QtWidgets.QApplication.translate("Form", "tx", None, -1))
        self.ty_checkBox.setText(QtWidgets.QApplication.translate("Form", "ty", None, -1))
        self.tz_checkBox.setText(QtWidgets.QApplication.translate("Form", "tz", None, -1))
        self.rotate_pushButton.setText(QtWidgets.QApplication.translate("Form", "Rotate", None, -1))
        self.rx_checkBox.setText(QtWidgets.QApplication.translate("Form", "rx", None, -1))
        self.ry_checkBox.setText(QtWidgets.QApplication.translate("Form", "ry", None, -1))
        self.rz_checkBox.setText(QtWidgets.QApplication.translate("Form", "rz", None, -1))
        self.ro_checkBox.setText(QtWidgets.QApplication.translate("Form", "ro", None, -1))
        self.ro_comboBox.setItemText(0, QtWidgets.QApplication.translate("Form", "XYZ", None, -1))
        self.ro_comboBox.setItemText(1, QtWidgets.QApplication.translate("Form", "YZX", None, -1))
        self.ro_comboBox.setItemText(2, QtWidgets.QApplication.translate("Form", "ZXY", None, -1))
        self.ro_comboBox.setItemText(3, QtWidgets.QApplication.translate("Form", "XZY", None, -1))
        self.ro_comboBox.setItemText(4, QtWidgets.QApplication.translate("Form", "YXZ", None, -1))
        self.ro_comboBox.setItemText(5, QtWidgets.QApplication.translate("Form", "ZYX", None, -1))
        self.scale_pushButton.setText(QtWidgets.QApplication.translate("Form", "Scale", None, -1))
        self.sx_checkBox.setText(QtWidgets.QApplication.translate("Form", "sx", None, -1))
        self.sy_checkBox.setText(QtWidgets.QApplication.translate("Form", "sy", None, -1))
        self.sz_checkBox.setText(QtWidgets.QApplication.translate("Form", "sz", None, -1))
        self.rotRefArray_groupBox.setTitle(QtWidgets.QApplication.translate("Form", "Rot Reference Array", None, -1))
        self.rotRefArrayAdd_pushButton.setText(QtWidgets.QApplication.translate("Form", "<<", None, -1))
        self.rotRefArrayRemove_pushButton.setText(QtWidgets.QApplication.translate("Form", ">>", None, -1))

