#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

"""
read serial output from Protek 506 multimeter and save it to file

(C) 2015 x4x georg.la8585@gmx.at

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

Name: Protek506_multimeter_RS232.py
Info:
Thema:
Date: <2015-05-06 Mittwoch 10:52>
Version:

the serial port configuration for the Protek506 is 1200,N,7,2.
Date is sent on sent enter.
"""

import datetime
import signal
import sys
import serial
import time


# open file
file = open("Protek_log.txt", "ab")

# open serial
ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=1200,
    bytesize=7,
    parity='N',
    stopbits=2,
    timeout=None,
    xonxoff=0,
    rtscts=0)


def signal_handler(signal, frame):
    """on Cont-C exit"""
    print 'You pressed Ctrl+C!'
    file.close()
    ser.close()
    sys.exit(0)

# run:
signal.signal(signal.SIGINT, signal_handler)

if(not ser.isOpen):
    ser.open()
print("serial is open")
counter = 0
while(ser.isOpen):
    counter += 1
    ser.write("\n")
    data = ser.read(1)
    data += ser.read(ser.inWaiting())
    datastr = (str(datetime.datetime.now()) + "  " + data)
    print(datastr)
    # append to fiel:
    file.write(datastr + "\n")
    """
    if counter > 20:  # every cycle
        file.flush()  # force writing to file
    """
    time.sleep(1)  # sleep 1sec
    
