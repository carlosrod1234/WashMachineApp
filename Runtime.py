#
# -*- coding: utf-8 -*-
# Designed on 14.05.2019
# Carlos Rodriguez
#
# Description:
# 1) Main RT system control
# 2) State Machines Control
#
#
#
"""
Created on Fri May 10 14:37:37 2019

@author: CARLOSPC
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
import sys
import os
import Main
import Menu
import Help
import tkinter.filedialog
from utils import *
import utils
import datetime
from IO_TCP import *
import IO_TCP
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os
import Loading
import subprocess, sys
from subprocess import Popen, PIPE

#cmd = r'C:\Users\CARLOSPC\Documents\Python\Grancentrix\Grandcentrix\Graphcentrix.exe'

class loadingApp(QtWidgets.QDialog, Loading.Ui_Dialog):
    #
    def __init__(self, parent=None):
        #
        super(helpapp, self).__init__(parent)
        self.setupUi(self)
        #
        # System Checks:
        # 1) Operative System
        # 2) PC Resources
        # 3) Internet COMM and open socket
        #
class helpapp(QtWidgets.QDialog, Help.Ui_Help):
    #
    def __init__(self, parent=None):
        #
        super(helpapp, self).__init__(parent)
        self.setupUi(self)
        self.Acept_help.clicked.connect(self.AcceptCommand)
        #
    def AcceptCommand(self,):
        #
        self.close()       
        #
class menuapp(QtWidgets.QDialog, Menu.Ui_IPConfig):
    #
    def __init__(self, parent=None):
        #
        super(menuapp, self).__init__(parent)
        self.setupUi(self)
        self.Acept.clicked.connect(self.AcceptCommand)
        self.Cancel.clicked.connect(self.CancelCommand)
        self.Clear_1.clicked.connect(self.Clear1)
        self.Clear_1.clicked.connect(self.Clear2)
        self.HostLine.setText(str(host_name))
        self.PortLine.setText(str(port_numb))
        #    
    def AcceptCommand(self,):
        #
        global host_name
        global port_numb
        #
        host_name = self.HostLine.text()
        port_numb = str(self.PortLine.text())
        self.close()       
        #
    def CancelCommand(self,):
        #
        self.close()
        #
    def Clear1(self,):
        #
        self.HostLine.clear()
        #
    def Clear2(self,): 
        #
        self.PortLine.clear()
        #
class uigrancentrix(QtWidgets.QMainWindow, Main.Ui_GrandCentrix):
    #
    def __init__(self, parent=None):
        #
        global _state
        _state = 0
        print(_state)
        #
        super(uigrancentrix, self).__init__(parent)
        #
        #QtWidgets.QMainWindow.setWindowFlags( QtCore.Qt.WindowCloseButtonHint )
        self.setupUi(self)
        #
        # Set Main Menu Values
        #
        #
        self.host_main.setText(str(host_name))
        self.port_main.setText(str(port_numb))
        #
        self.Clear_command.clicked.connect(self.clearCommand)
        self.Clear_logger.clicked.connect(self.clearLogger)
        self.Send_Command.clicked.connect(self.sendCommand)
        self.Upload.clicked.connect(self.UploadIP)
        self.dummy = False
        #
        # MenuBar items (needs to be redone)
        #
        bar = self.menuBar()
        config = bar.addMenu("Menu")
        config.addAction("Config IP")
        config.triggered[QtWidgets.QAction].connect(self.MenuHandler)
        #
        about = bar.addMenu("About")
        about.addAction("Help")
        about.triggered[QtWidgets.QAction].connect(self.HelpHandler)
        #
        #os.system("Graphcentrix.exe")
        #subprocess.run(["Graphcentrix.exe"])
        self.IP_host ="127.0.0.1"
        self.IP_port =65432
        #self.io_tcp = IO_comm(self.IP_host, self.IP_port,1, "datalog", "w")
       # status = self.io_tcp.runtimeState("")
        #self.Logger_writting.append("->" + str(status)+"\r")
        #
        self.io_tcp = IO_comm(self.IP_host, self.IP_port,1, "datalog", "w")
        self.IO_txt_ = IO_txt(str("RunTimedatalog")+".txt","w")
        #
        # 1 - Open socket
        # 2 - check status 
        # 3 - Start dummy if not slave
        # 4 - Start comunication if there are slave
        # 5 - start dummy if the comunication is lost
        #
        #subprocess.Popen(['Graphcentrix.exe']).communicate()
       #result = os.popen("Graphcentrix.exe").read()
    def sendCommand(self,):
        #
        # Send Command
        #
        root = tkinter.Tk()
        root.withdraw()
        txtbox = self.CommandSend.text().upper()
        #
        if len(txtbox) != 0:
            #
            self.Logger_writting.append("->" + str(datetime.datetime.now())+" Send data: " + txtbox + "\r")
            self.IO_txt_.writetxt(str(datetime.datetime.now()) + " " +str(txtbox)+" data RCV"+"\r")
            #
            for i in range (0,2):
               #
               rdata,rawdata = self.io_tcp.runtimeState(str(txtbox))
               #
               print(rdata)
               print(rawdata)
               #
               #self.CommandSend_2.value(rdata)
               #
               self.Logger_writting.append("->" + str(datetime.datetime.now())+" Return data: " + str(rdata) + "\r")
               self.IO_txt_.writetxt(str(datetime.datetime.now()) + " " +str(rdata)+" data RCV"+"\r")
               self.Commandrcv.setText(str(rawdata))
               #
        else: 
            self.Logger_writting.append("->" + str(datetime.datetime.now())+" Empty Command Line"  + "\r")
            self.IO_txt_.writetxt(str(datetime.datetime.now()) + " Empty Command Line"+"\r")
        #
    def clearCommand(self,):
        #
        # Clear command send dialog
        #
        self.Commandrcv.clear()
        self.CommandSend.clear()
        self.IO_txt_.writetxt(str(datetime.datetime.now()) + " " +"Clear Data"+"\r")
        #
    def clearLogger(self,):
        #
        # Clear Logger content
        #
        self.Logger_writting.clear()
        self.IO_txt_.writetxt(str(datetime.datetime.now()) + " " +"Clear Logger"+"\r")
        #
    def MenuHandler(self):
        #
        menu = menuapp(self)
        menu.setWindowModality(QtCore.Qt.ApplicationModal)
        self.IO_txt_.writetxt(str(datetime.datetime.now()) + " " +"Open Menu"+"\r")
        menu.show()
        #
    def UploadIP(self):
        #
        # Update Tables
        #
        global host_name
        global port_numb
        #
        self.host_main.setText(str(host_name))
        self.port_main.setText(str(port_numb))
        self.io_tcp = IO_comm(self.IP_host, self.IP_port,1, "datalog", "w")
        #
        for i in range(0,2):
            #
            status, temp = self.io_tcp.runtimeState("GCVCNP") 
            self.Logger_writting.append("->" + str(status)+"\r")
            #
        self.IO_txt_.writetxt(str(datetime.datetime.now()) + " " +"Upload IP Menu"+"\r")
        #
    def HelpHandler(self):
        #
        menu = helpapp(self) 
        menu.setWindowModality(QtCore.Qt.ApplicationModal)
        self.IO_txt_.writetxt(str(datetime.datetime.now()) + " " +"Open Help & Support"+"\r")
        menu.show()
        #
def main():
    #
    app = QtWidgets.QApplication(sys.argv)
    form = uigrancentrix()
    form.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)
    form.show()
    app.exec_()
    #
if __name__ == '__main__':
    main()