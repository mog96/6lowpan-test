import socket
from time import sleep

while 1:
  s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
  s.sendto('helloworld'.encode('utf-8'), ('10.8.0.2', 12345))
  sleep(2)