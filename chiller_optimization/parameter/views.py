import struct
from django.shortcuts import render
import snap7
from snap7.util import *

plc = snap7.client.client()
ip_address = '192.168.0.1'
rack = 2
slot = 1 


db_number = 2
ct_out_address = 9
ch_in_address = 10

def readtemp(ip_address, db_number,ct_out_address, ch_in_address):
   
    plc.connect(ip_address, rack, slot) 
       
    if plc.get_connected():
        data1 = plc.db_read(db_number, ct_out_address , 4)
        ct_out_temp_pv = struct.unpack('>f', data1)[0]
        data2 = plc.db_read(db_number, ch_in_address , 4)
        ch_in_temp_pv = struct.unpack('>f', data2)[0]
        diff_temp = abs(data1-data2)
        return diff_temp
        
    else:
        print("unable to connect to plc.")
    
       
        

            

            
       
    




    
            
   