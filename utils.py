# -*- coding: utf-8 -*-
#
# -*- coding: utf-8 -*-
# Designed on 14.05.2019
# Carlos Rodriguez
#
# Description:
# 1) Logger .txt control
# 2) Sockets control
#
#
#
"""
Created on Fri May 10 09:13:34 2019

@author: CARLOSPC
"""
# Echo client program
import socket
import sys
import time
import os
#
global host_name
#
host_name = "127.0.0.1"
global port_numb
port_numb = 1201
#
class IP_Comm():
    #
    def __init__(self,host, port, status):
        #
        self.HOST = host
        self.PORT = port
        self.satus_ = status
        # self.addr_ =""
        #  self.conn_ =""
        self.msg=""
        self.sock_= ""
        self.connection_=""
        self.client_address_=""
        #
    def open_socket (self,):
        #
        global _state
        global socket
        HOST = host_name  # Standard loopback interface address (localhost)
        PORT = port_numb       # Port to listen on (non-privileged ports are > 1023)
        #
        # Open .exe
        #
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.sock_:
            #
            self.sock_.bind((HOST, PORT))
            self.sock_.listen()
            self.sock_.settimeout(2)
            print(str(HOST)+" "+str(PORT))
            #
            while 1:
                #
                try:
                    #
                    self.conn, self.addr = self.sock_.accept()
                    #
                    data = self.conn.recv(8)
                    #
                    if str(data).find("START") >= 0:
                        #
                        connected = 'Connected by' + str(self.addr)
                        _state = 1
                        print(_state)
                        return False, str(self.addr),self.conn
                    else:
                        #
                        print(_state)
                        _state = 0
                        return True,"",self.conn
                        #
                except socket.timeout:
                    #
                    connected = 'No Slave -> Dummy Mode Transmition'
                    print(connected)
                    return True, "",""
                    #
    def open_socket2 (self,):
        #
        global _state
        global socket
        HOST = host_name  # Standard loopback interface address (localhost)
        PORT = port_numb       # Port to listen on (non-privileged ports are > 1023)
        #
        # Open .exe
        #
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.sock_:
            #
            self.sock_.bind((HOST, PORT))
            self.sock_.listen()
            print(str(HOST)+" "+str(PORT))
            self.conn, self.addr = self.sock_.accept()
            #
    def send_data (self, data,conn):
        #
        global _state
        global socket
        #
        try:
            print ("send data " + str(data))
            conn.send(data.encode('utf-8'))
        except:
            _state = 3
            print("Socket came down")
        #
    def rcv_data (self, conn):   
        #
        global _state
        global socket        
        #
        try:
            print("data rcv")
            data = conn.recv(8)
            print("data2")
            return data
        except:
            #
            _state = 3
            print("Socket came down")
            #
    def sock_close(self,):
        #
        self.conn_.close()
        #

class IO_txt():
    #
    def __init__(self,filename, wr):
        #
        self.filename_ = filename
        self.wr_ = wr
        self.file =""
        #
        try:
            #
            self.file_ = open(str(self.filename_), str(self.wr_))
            #
        except IOError:
            #
            print("Error open file" + str(self.file_))
            return 0
            #   
    def writetxt(self,data):
        #
        try:
            #
            self.file_.write(data)
            #
        except IOError:
            print("Error write file" + str(self.file_))
            return 0
            #
    def readtxt(self,):
        #
        try: 
            #
            data = self.file_.read()
            return data
            #
        except IOError:
            print("Error read file" + str(self.file_))
            return 0
            #
    def closetxt(self,):
        #
        try: 
            #
            self.file_.close()
            #
        except IOError:
            print("Error close file file ! " + str(self.file_))
            return 0

if __name__ == '__main__':
   #txt_ = IO_txt()
   ip_ = IP_Comm(host_name,port_numb,True)
   data = ip_.open_socket2()
   ip_.send_data("dataout")
   