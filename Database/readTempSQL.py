#! /usr/bin/env python
import serial
import os
import time
import datetime
import glob
import MySQLdb
from time import strftime

ser = serial.Serial('/dev/ttyACM0', 9600)

# Variables for MySQL
db = MySQLdb.connect(host="localhost", user="test", passwd="raspberry", db="temp_database")
cur = db.cursor()
 
def tempRead():
    line = ser.readline()
    line = line.center(4)
    return line

while True:
    temp = tempRead()
    print(temp)
    datetimeWrite = (time.strftime("%Y-%m-%d ") + time.strftime("%H:%M:%S"))
    print(datetimeWrite)
    sql = ("""INSERT INTO tempLog (datetime,temperature) VALUES (%s,%s)""",(datetimeWrite,temp))
    try:
        print("Writing to database...")
        # Execute the SQL command
        cur.execute(*sql)
        # Commit your changes in the database
        db.commit()
        print("Write Complete")
 
    except:
        # Rollback in case there is any error
        db.rollback()
        print("Failed writing to database")
 
    cur.close()
    db.close()
    break
