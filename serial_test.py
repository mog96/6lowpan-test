#!/usr/bin/python
# Get lines of text from serial port, save them to a file.

import datetime
import serial
import sys

addr  = '/dev/ttyUSB0'                                 # serial port to read data from
baud  = 128000                                         # baud rate for serial port
fname = 'logs/log' + datetime.datetime.now() + '.txt'  # log file to save data in
fmode = 'a'                                            # log file mode = APPEND

with serial.Serial(addr, baud) as ser, open(fname, fmode) as f:
    while (1):
        x = ser.read()         # read one line of text from serial port
        sys.stdout.write(x)    # echo byte on-screen as ASCII
        sys.stdout.flush()     # make sure it actually gets written out
        f.write(x)             # write line of text to file
        f.flush()              # make sure it actually gets written out