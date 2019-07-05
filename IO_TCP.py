# -*- coding: utf-8 -*-
#
# -*- coding: utf-8 -*-
# Designed on 14.05.2019
# Carlos Rodriguez
#
# Description:
# 1) IO Comm interfaces Control
#
#
#
"""
Created on Fri May 10 15:04:22 2019

@author: CARLOSPC
"""

import sys
from utils import IP_Comm
from utils import IO_txt
import datetime
import time
from Runtime import *
from globalsval import *
import Runtime
import utils

global _state
_state=0
global state_list
state_list = []
class IO_comm():
    #
    def __init__(self,host,port,status, filename, wr):   
        #
        global _state
        self.host_= host
        self.port_= port
        self.status_= status
        self.filename_ =filename
        self.wr_ = wr
        #
        #   Class constructor
        #
        #self.IO_txt_ = IO_txt(str(self.filename_)+".txt",str(self.wr_))
        #
        # Start execution state machinesglobal STATE 
        #self.IP_comm_.open_socket(self.host_, self.port_)
        #
    def runtimeOperation(self, data_command):
        #
        crc = 0
        ln = 0
        #
        if data_command != "":
            #
            if data_command == "HELLO":
                #
                dat = [10, 5, 1]
                cmd = 1
                #
            elif data_command == "GET_MACHINE_INFO":
                #
                dat = [10, 5, 2]
                cmd = 2
                #
            elif data_command == "GET STATUS":
                #
                dat = [10, 5, 3]
                cmd = 3
                #
            elif data_command == "START_PROGRAM":
                #
                dat = [10, 5, 4]
                cmd = 4
                #
            elif data_command == "ABORT_PROGRAM":
                #
                dat = [10, 5, 5]
                cmd = 5
                #
            else:
                #
                msg = "ERR CMD"
                return msg, msg
                #
            #
            #  The transmitted command frame is based on bellow structure:
            #
            #  CRC/LEN/SEQ
            #
            #
            #crc_tx =self.crc8(dat)
            #
            if data_command != "":
                #
                ln = 4
                #
                tx = str(dat[0])+str(dat[1])+str(dat[2])
                print("The data tx is: " + tx)
                #
                conn_ = IP_Comm(host_name,port_numb,1)
                #self.IO_txt_.writetxt(str(datetime.datetime.now()) + " " +tx+" data transmitted"+"\r")
                conn_.send_data (tx,self.conn)
                time.sleep(0.100) #Delay 100mS.
                rcv = str(conn_.rcv_data(self.conn))
                print(str(rcv))
                #
            if rcv != "":
                #
                rcv_frame =[]
                rcv_frame_numb =[]
                rcv_frame.append("CRC ->" + (rcv[2] + rcv[3]))
                rcv_frame.append("LEN ->" + (rcv[4]))
                rcv_frame.append("DATA ->" + (rcv[5]) + rcv[6])
                print(rcv_frame)
                rcv_frame_numb.append((rcv[2] + rcv[3]))
                rcv_frame_numb.append((rcv[4]))
                rcv_frame_numb.append((rcv[5]) + rcv[6])
                #
            else:
                #
                # 2 - Error State 
                #
                #self.IO_txt_.writetxt(str(datetime.datetime.now()) + " " + str(rcv)+" data received"+"\r")
                msg = "ERR RCV CMD"
                return msg, msg
            #
            return (rcv_frame, rcv_frame_numb)
                #
        #crc_rx =self.crc8(rcv_frame)
        #
        #if(crc_rx == hex(rcv[0])):
            #
            #Match CRC return the full message
            #
            #return msg
            #
       # else:
            #
           # msg = "Error CRC"
            #
           # return msg
            #  
    def dummyruntimeOperation(self, data_command):
        #
        while data_command != "EXPLOTE":
            #
            if data_command == "HELLO":
                #
                dat = ["1", "0", "5", "1", "1"]
                cmd = 0x01
                #
            elif data_command == "GET_MACHINE_INFO":
                #
                dat = ["1", "0", "5", "2", "1"]
                cmd = 0x02
                #
            elif data_command == "GET STATUS":
                #
                dat = ["1", "0", "5", "3", "1"]
                cmd = 0x3
                #
            elif data_command == "START_PROGRAM":
                #
                dat = ["1", "0", "5", "4", "1"]
                cmd = 0x04
                #
            elif data_command == "ABORT_PROGRAM":
                #
                dat = ["1", "0", "5", "5", "1"]
                cmd = 0x05
                #
            else:
                #
                msg = "ERR CMD",""
            
            if data_command != "":
                #
                rcv_frame =[]
                rcv_frame_numb =[]
                rcv_frame.append("CRC ->" + (dat[0] + dat[1]))
                rcv_frame.append("LEN ->" + (dat[2]))
                rcv_frame.append("DATA ->" + (dat[3]) + dat[4])
                print(rcv_frame)
                rcv_frame_numb.append(dat[0] + dat[1])
                rcv_frame_numb.append(dat[2])
                rcv_frame_numb.append(dat[3] + dat[4])      
                
                #self.IO_txt_.writetxt(str(datetime.datetime.now()) + " " + str(rcv_frame_numb)+" data received"+"\r")
    
                return (rcv_frame, rcv_frame_numb)
        #
            #crc =self.crc8(dat)
            #
            #ln = 4
            #
            #tx = str(hex(crc)).replace("0x","")+str(hex(ln)).replace("0x","")+str(hex(cmd)).replace("0x","")
            #
            #self.IO_txt_.writetxt(str(datetime.datetime.now()) + ": The transmitted data is: " + str(tx) + "\r")
            #print("The transmitted data is: " + str(tx))
            #
            #return tx
            #                            
    def runtimeState(self, data_command):
        #
        global host_name
        global port_numb
        global _state
        #
        if (_state == 0):
            #
            # State is in iddle mode
            #
            #print(str(host_name) + " " +str(port_numb))
            self.IP_comm_ = IP_Comm(host_name,port_numb,1)
            error, addr,self.conn= self.IP_comm_.open_socket()
            #
            if error == False:
                #
                # RT Mode
                #
                print ("RT")
                _state = 1
                #self.IO_txt_.writetxt(str(datetime.datetime.now()) + ": COM ENABLED" +" RT Mode Enable Address:"+ str(addr)  + "\r")
                return ("->" + "COM ENABLED" +" RT Mode Enable Address:"+ str(addr)  + "\r") , ""
                #
            else:
                #
                # Dummy mode
                #
                 print ("Dummy")
                 _state = 2
                 #self.IO_txt_.writetxt(str(datetime.datetime.now()) + ": COM ENABLED" +"NO INTERNET COMM."+" DUMMY Mode Enable"  + "\r")
                 return ("->" + "NO INTERNET COMM."+" DUMMY Mode Enable"  + "\r") , ""          
                #
            #self.IO_txt_.writetxt(str(datetime.datetime.now()) + ": " + "Iddle State"+"\r")
            #
        elif(_state == 1):
            #
            # State is in running mode
            # Running mode is defined like:
            # Pooling status is working
            # command send/received is accepted
            #
            if (data_command == "GCVCNP"):
                #
                print("restart")
                _state = 0
                print(state_list)
                return "Updated Communication"  + "\r", ""
                #
            else:   
                print ("state1 RT")
                msg, msg2 = self.runtimeOperation(data_command)
                #
                return msg, msg2
            #
        elif(_state ==2):
            #
            #state is in error mode
            #
            if (data_command == "GCVCNP"):
                #
                _state = 0
                return "Updated Communication"  + "\r", ""
                #
                #
            else:   
                print ("Dummmy")
                msg, msg2 = self.dummyruntimeOperation(data_command)
                #self.IO_txt_.writetxt(str(datetime.datetime.now()) + ": Dummy Data TX/RX " + str(msg) +"\r")
                #
                return msg, msg2
            #
        elif(_state == 3): 
            #
            #state is in error mode
            #
            msg = "Error Communication" + "\r"
            _state = 0
            #self.IO_txt_.writetxt(str(datetime.datetime.now()) + ": Error Mode " + str(data_command)+"\r")
            #
            return msg
            #            
    def crc8(self,buff):
        #
        crc = 0
        #
        for b in buff:
            crc ^= b
            for i in range(8):
                if crc & 1:
                    crc = (crc >> 1) ^ 0x8C
                else:
                    crc >>= 1
        return crc

if __name__ == '__main__':
    comm = IO_comm('127.0.0.1',65432,"", "datalog", "w") 
    comm.runtimeState("")
    comm.runtimeState("HELLO")
      