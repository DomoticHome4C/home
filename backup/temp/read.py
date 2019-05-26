import serial
import os
import time
import datetime
import glob
from time import strftime

ser = serial.Serial('/dev/ttyACM0', 9600)

def tempRead():
        line = ser.readline()
        line = line.center(4)
        return line
    
while True:
    temp = tempRead()
    print(temp)
    datetimeWrite = (time.strftime("%Y-%m-%d ") + time.strftime("%H:%M:%S"))
    print(datetimeWrite)
    break

