# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/Projects/Pipeline/rez-packages/third/github.com/yamahigashi/ymtshiftercomponents/mgear_shifter_components/python/ymt_components/ymt_spine_ik_03/settingsUI.ui',
# licensing of 'D:/Projects/Pipeline/rez-packages/third/github.com/yamahigashi/ymtshiftercomponents/mgear_shifter_components/python/ymt_components/ymt_spine_ik_03/settingsUI.ui' applies.
#
# Created: Sun May 29 15:07:53 2022
#      by: pyside2-uic  running on PySide2 5.12.5
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(419, 780)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fkNb_label = QtWidgets.QLabel(self.groupBox_3)
        self.fkNb_label.setMinimumSize(QtCore.QSize(300, 0))
        self.fkNb_label.setObjectName("fkNb_label")
        self.horizontalLayout_2.addWidget(self.fkNb_label)
        self.fkNb_spinBox = QtWidgets.QSpinBox(self.groupBox_3)
        self.fkNb_spinBox.setMinimumSize(QtCore.QSize(50, 0))
        self.fkNb_spinBox.setMinimum(2)
        self.fkNb_spinBox.setMaximum(999)
        self.fkNb_spinBox.setProperty("value", 5)
        self.fkNb_spinBox.setObjectName("fkNb_spinBox")
        self.horizontalLayout_2.addWidget(self.fkNb_spinBox)
        self.horizontalLayout_2.setStretch(0, 1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.surplusFkNb_label = QtWidgets.QLabel(self.groupBox_3)
        self.surplusFkNb_label.setMinimumSize(QtCore.QSize(300, 0))
        self.surplusFkNb_label.setObjectName("surplusFkNb_label")
        self.horizontalLayout.addWidget(self.surplusFkNb_label)
        self.surplusFkNb_spinBox = QtWidgets.QSpinBox(self.groupBox_3)
        self.surplusFkNb_spinBox.setMinimumSize(QtCore.QSize(50, 0))
        self.surplusFkNb_spinBox.setObjectName("surplusFkNb_spinBox")
        self.horizontalLayout.addWidget(self.surplusFkNb_spinBox)
        self.horizontalLayout.setStretch(0, 1)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.overrideNegate_checkBox = QtWidgets.QCheckBox(Form)
        self.overrideNegate_checkBox.setText("Override Negate Axis Direction For \"R\" Side")
        self.overrideNegate_checkBox.setObjectName("overrideNegate_checkBox")
        self.verticalLayout.addWidget(self.overrideNegate_checkBox)
        self.addJoints_checkBox = QtWidgets.QCheckBox(Form)
        self.addJoints_checkBox.setText("Add Joints")
        self.addJoints_checkBox.setChecked(True)
        self.addJoints_checkBox.setObjectName("addJoints_checkBox")
        self.verticalLayout.addWidget(self.addJoints_checkBox)
        self.isSplitHip_checkBox = QtWidgets.QCheckBox(Form)
        self.isSplitHip_checkBox.setText("Split Hip Fk control from others.")
        self.isSplitHip_checkBox.setChecked(True)
        self.isSplitHip_checkBox.setObjectName("isSplitHip_checkBox")
        self.verticalLayout.addWidget(self.isSplitHip_checkBox)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.softness_label = QtWidgets.QLabel(Form)
        self.softness_label.setObjectName("softness_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.softness_label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.softness_slider = QtWidgets.QSlider(Form)
        self.softness_slider.setMinimumSize(QtCore.QSize(0, 15))
        self.softness_slider.setMaximum(100)
        self.softness_slider.setOrientation(QtCore.Qt.Horizontal)
        self.softness_slider.setObjectName("softness_slider")
        self.horizontalLayout_3.addWidget(self.softness_slider)
        self.softness_spinBox = QtWidgets.QSpinBox(Form)
        self.softness_spinBox.setMaximum(100)
        self.softness_spinBox.setObjectName("softness_spinBox")
        self.horizontalLayout_3.addWidget(self.softness_spinBox)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.softness_label_2 = QtWidgets.QLabel(Form)
        self.softness_label_2.setObjectName("softness_label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.softness_label_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.position_slider = QtWidgets.QSlider(Form)
        self.position_slider.setMinimumSize(QtCore.QSize(0, 15))
        self.position_slider.setMaximum(100)
        self.position_slider.setOrientation(QtCore.Qt.Horizontal)
        self.position_slider.setObjectName("position_slider")
        self.horizontalLayout_4.addWidget(self.position_slider)
        self.position_spinBox = QtWidgets.QSpinBox(Form)
        self.position_spinBox.setMaximum(100)
        self.position_spinBox.setObjectName("position_spinBox")
        self.horizontalLayout_4.addWidget(self.position_spinBox)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.maxStretch_label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxStretch_label.sizePolicy().hasHeightForWidth())
        self.maxStretch_label.setSizePolicy(sizePolicy)
        self.maxStretch_label.setObjectName("maxStretch_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.maxStretch_label)
        self.maxStretch_spinBox = QtWidgets.QDoubleSpinBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxStretch_spinBox.sizePolicy().hasHeightForWidth())
        self.maxStretch_spinBox.setSizePolicy(sizePolicy)
        self.maxStretch_spinBox.setMinimum(1.0)
        self.maxStretch_spinBox.setSingleStep(0.1)
        self.maxStretch_spinBox.setProperty("value", 1.0)
        self.maxStretch_spinBox.setObjectName("maxStretch_spinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.maxStretch_spinBox)
        self.maxSquash_label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxSquash_label.sizePolicy().hasHeightForWidth())
        self.maxSquash_label.setSizePolicy(sizePolicy)
        self.maxSquash_label.setObjectName("maxSquash_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.maxSquash_label)
        self.maxSquash_spinBox = QtWidgets.QDoubleSpinBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxSquash_spinBox.sizePolicy().hasHeightForWidth())
        self.maxSquash_spinBox.setSizePolicy(sizePolicy)
        self.maxSquash_spinBox.setMinimum(0.1)
        self.maxSquash_spinBox.setMaximum(1.0)
        self.maxSquash_spinBox.setSingleStep(0.1)
        self.maxSquash_spinBox.setProperty("value", 1.0)
        self.maxSquash_spinBox.setObjectName("maxSquash_spinBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.maxSquash_spinBox)
        self.verticalLayout.addLayout(self.formLayout)
        self.ikProfile_pushButton = QtWidgets.QPushButton(Form)
        self.ikProfile_pushButton.setObjectName("ikProfile_pushButton")
        self.verticalLayout.addWidget(self.ikProfile_pushButton)
        self.ik0RefArray_groupBox = QtWidgets.QGroupBox(Form)
        self.ik0RefArray_groupBox.setObjectName("ik0RefArray_groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.ik0RefArray_groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.ik0RefArray_horizontalLayout = QtWidgets.QHBoxLayout()
        self.ik0RefArray_horizontalLayout.setObjectName("ik0RefArray_horizontalLayout")
        self.ik0RefArray_verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.ik0RefArray_verticalLayout_1.setObjectName("ik0RefArray_verticalLayout_1")
        self.ik0RefArray_listWidget = QtWidgets.QListWidget(self.ik0RefArray_groupBox)
        self.ik0RefArray_listWidget.setDragDropOverwriteMode(True)
        self.ik0RefArray_listWidget.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.ik0RefArray_listWidget.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.ik0RefArray_listWidget.setAlternatingRowColors(True)
        self.ik0RefArray_listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.ik0RefArray_listWidget.setSelectionRectVisible(False)
        self.ik0RefArray_listWidget.setObjectName("ik0RefArray_listWidget")
        self.ik0RefArray_verticalLayout_1.addWidget(self.ik0RefArray_listWidget)
        self.ik0RefArray_horizontalLayout.addLayout(self.ik0RefArray_verticalLayout_1)
        self.ik0RefArray_verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.ik0RefArray_verticalLayout_2.setObjectName("ik0RefArray_verticalLayout_2")
        self.ik0RefArrayAdd_pushButton = QtWidgets.QPushButton(self.ik0RefArray_groupBox)
        self.ik0RefArrayAdd_pushButton.setObjectName("ik0RefArrayAdd_pushButton")
        self.ik0RefArray_verticalLayout_2.addWidget(self.ik0RefArrayAdd_pushButton)
        self.ik0RefArrayRemove_pushButton = QtWidgets.QPushButton(self.ik0RefArray_groupBox)
        self.ik0RefArrayRemove_pushButton.setObjectName("ik0RefArrayRemove_pushButton")
        self.ik0RefArray_verticalLayout_2.addWidget(self.ik0RefArrayRemove_pushButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.ik0RefArray_verticalLayout_2.addItem(spacerItem)
        self.ik0RefArray_horizontalLayout.addLayout(self.ik0RefArray_verticalLayout_2)
        self.gridLayout_3.addLayout(self.ik0RefArray_horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.ik0RefArray_groupBox)
        self.ik1RefArray_groupBox = QtWidgets.QGroupBox(Form)
        self.ik1RefArray_groupBox.setObjectName("ik1RefArray_groupBox")
        self.gridLayout_31 = QtWidgets.QGridLayout(self.ik1RefArray_groupBox)
        self.gridLayout_31.setObjectName("gridLayout_31")
        self.ik1RefArray_horizontalLayout = QtWidgets.QHBoxLayout()
        self.ik1RefArray_horizontalLayout.setObjectName("ik1RefArray_horizontalLayout")
        self.ik1RefArray_verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.ik1RefArray_verticalLayout_1.setObjectName("ik1RefArray_verticalLayout_1")
        self.ik1RefArray_listWidget = QtWidgets.QListWidget(self.ik1RefArray_groupBox)
        self.ik1RefArray_listWidget.setDragDropOverwriteMode(True)
        self.ik1RefArray_listWidget.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.ik1RefArray_listWidget.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.ik1RefArray_listWidget.setAlternatingRowColors(True)
        self.ik1RefArray_listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.ik1RefArray_listWidget.setSelectionRectVisible(False)
        self.ik1RefArray_listWidget.setObjectName("ik1RefArray_listWidget")
        self.ik1RefArray_verticalLayout_1.addWidget(self.ik1RefArray_listWidget)
        self.ik1RefArray_horizontalLayout.addLayout(self.ik1RefArray_verticalLayout_1)
        self.ik1RefArray_verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.ik1RefArray_verticalLayout_2.setObjectName("ik1RefArray_verticalLayout_2")
        self.ik1RefArrayAdd_pushButton = QtWidgets.QPushButton(self.ik1RefArray_groupBox)
        self.ik1RefArrayAdd_pushButton.setObjectName("ik1RefArrayAdd_pushButton")
        self.ik1RefArray_verticalLayout_2.addWidget(self.ik1RefArrayAdd_pushButton)
        self.ik1RefArrayRemove_pushButton = QtWidgets.QPushButton(self.ik1RefArray_groupBox)
        self.ik1RefArrayRemove_pushButton.setObjectName("ik1RefArrayRemove_pushButton")
        self.ik1RefArray_verticalLayout_2.addWidget(self.ik1RefArrayRemove_pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.ik1RefArray_verticalLayout_2.addItem(spacerItem1)
        self.ik1RefArray_horizontalLayout.addLayout(self.ik1RefArray_verticalLayout_2)
        self.gridLayout_31.addLayout(self.ik1RefArray_horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.ik1RefArray_groupBox)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.groupBox_3.setTitle(QtWidgets.QApplication.translate("Form", "FK Controls", None, -1))
        self.fkNb_label.setText(QtWidgets.QApplication.translate("Form", "FK Ctl Number", None, -1))
        self.surplusFkNb_label.setText(QtWidgets.QApplication.translate("Form", "Rib Cage FK Number", None, -1))
        self.isSplitHip_checkBox.setToolTip(QtWidgets.QApplication.translate("Form", "<html><head/><body><p>If checked each controller is free from its parent xform.</p></body></html>", None, -1))
        self.softness_label.setText(QtWidgets.QApplication.translate("Form", "Softness", None, -1))
        self.softness_label_2.setText(QtWidgets.QApplication.translate("Form", "Position", None, -1))
        self.maxStretch_label.setText(QtWidgets.QApplication.translate("Form", "Max Stretch", None, -1))
        self.maxSquash_label.setText(QtWidgets.QApplication.translate("Form", "Max Squash", None, -1))
        self.ikProfile_pushButton.setText(QtWidgets.QApplication.translate("Form", "Squash and Stretch Profile", None, -1))
        self.ik0RefArray_groupBox.setTitle(QtWidgets.QApplication.translate("Form", "ik0 Reference Array", None, -1))
        self.ik0RefArrayAdd_pushButton.setText(QtWidgets.QApplication.translate("Form", "<<", None, -1))
        self.ik0RefArrayRemove_pushButton.setText(QtWidgets.QApplication.translate("Form", ">>", None, -1))
        self.ik1RefArray_groupBox.setTitle(QtWidgets.QApplication.translate("Form", "ik1 Reference Array", None, -1))
        self.ik1RefArrayAdd_pushButton.setText(QtWidgets.QApplication.translate("Form", "<<", None, -1))
        self.ik1RefArrayRemove_pushButton.setText(QtWidgets.QApplication.translate("Form", ">>", None, -1))

