# -*- coding: utf-8 -*-
#
# -*- coding: utf-8 -*-
# Designed on 14.05.2019
# Carlos Rodriguez
#
# Description:
# 1) Loading data control
#
#
#

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(378, 503)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(60, 50, 271, 281))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.Logger_writting_2 = QtWidgets.QTextBrowser(Dialog)
        self.Logger_writting_2.setGeometry(QtCore.QRect(30, 360, 321, 121))
        self.Logger_writting_2.setObjectName("Logger_writting_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:6pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/Logo/Info.jpg\" /></p></body></html>"))


