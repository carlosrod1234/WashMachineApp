# -*- coding: utf-8 -*-
#
# -*- coding: utf-8 -*-
# Designed on 14.05.2019
# Carlos Rodriguez
#
# Description:
# 1) Help & Support interface PyQT
#
#
#
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Help(object):
    def setupUi(self, Help):
        Help.setObjectName("Help")
        Help.resize(389, 523)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Info.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Help.setWindowIcon(icon)
        self.textBrowser = QtWidgets.QTextBrowser(Help)
        self.textBrowser.setGeometry(QtCore.QRect(60, 40, 271, 281))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.Acept_help = QtWidgets.QPushButton(Help)
        self.Acept_help.setGeometry(QtCore.QRect(40, 470, 311, 31))
        self.Acept_help.setObjectName("Acept_help")
        self.textEdit = QtWidgets.QTextEdit(Help)
        self.textEdit.setGeometry(QtCore.QRect(60, 350, 271, 101))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Help)
        QtCore.QMetaObject.connectSlotsByName(Help)

    def retranslateUi(self, Help):
        _translate = QtCore.QCoreApplication.translate
        Help.setWindowTitle(_translate("Help", "Help & Support"))
        self.textBrowser.setHtml(_translate("Help", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:6pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"Info.jpg\" /></p></body></html>"))
        self.Acept_help.setText(_translate("Help", "Accept"))
        self.textEdit.setHtml(_translate("Help", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline; color:#00007f;\">DESCRIPTION:</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#00007f;\">Product: GUI Grandcentrix</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#00007f;\">Designer: Carlos Rodriguez Calvo</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#00007f;\">Version: 000.000.001</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#00007f;\">Date: 14.05.2019</span></p></body></html>"))


#import graph_rc
