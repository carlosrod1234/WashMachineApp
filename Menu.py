# -*- coding: utf-8 -*-
#
# -*- coding: utf-8 -*-
# Designed on 14.05.2019
# Carlos Rodriguez
#
# Description:
# 1) Manu interface PyQT
#
#
#

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_IPConfig(object):
    def setupUi(self, IPConfig):
        IPConfig.setObjectName("IPConfig")
        IPConfig.resize(297, 242)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Info.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        IPConfig.setWindowIcon(icon)
        self.PortLine = QtWidgets.QLineEdit(IPConfig)
        self.PortLine.setGeometry(QtCore.QRect(30, 60, 151, 31))
        self.PortLine.setObjectName("PortLine")
        self.label = QtWidgets.QLabel(IPConfig)
        self.label.setGeometry(QtCore.QRect(80, 40, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.HostLine = QtWidgets.QLineEdit(IPConfig)
        self.HostLine.setGeometry(QtCore.QRect(30, 120, 151, 31))
        self.HostLine.setObjectName("HostLine")
        self.label_2 = QtWidgets.QLabel(IPConfig)
        self.label_2.setGeometry(QtCore.QRect(80, 100, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Acept = QtWidgets.QPushButton(IPConfig)
        self.Acept.setGeometry(QtCore.QRect(20, 180, 111, 31))
        self.Acept.setObjectName("Acept")
        self.Cancel = QtWidgets.QPushButton(IPConfig)
        self.Cancel.setGeometry(QtCore.QRect(170, 180, 111, 31))
        self.Cancel.setObjectName("Cancel")
        self.Clear_2 = QtWidgets.QPushButton(IPConfig)
        self.Clear_2.setGeometry(QtCore.QRect(190, 120, 91, 31))
        self.Clear_2.setObjectName("Clear_2")
        self.Clear_1 = QtWidgets.QPushButton(IPConfig)
        self.Clear_1.setGeometry(QtCore.QRect(190, 60, 91, 31))
        self.Clear_1.setObjectName("Clear_1")

        self.retranslateUi(IPConfig)
        QtCore.QMetaObject.connectSlotsByName(IPConfig)

    def retranslateUi(self, IPConfig):
        _translate = QtCore.QCoreApplication.translate
        IPConfig.setWindowTitle(_translate("IPConfig", "Menu"))
        self.label.setText(_translate("IPConfig", "Port"))
        self.label_2.setText(_translate("IPConfig", "Host"))
        self.Acept.setText(_translate("IPConfig", "Accept"))
        self.Cancel.setText(_translate("IPConfig", "Cancel"))
        self.Clear_2.setText(_translate("IPConfig", "Clear"))
        self.Clear_1.setText(_translate("IPConfig", "Clear"))


