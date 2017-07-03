import serial

ser = serial.Serial("/dev/ttyUSB0", baudrate=12800, timeout=1.0)
print 'READING FROM PORT', ser.name

while True:
    byte = ser.read() # read one byte
    print byte