import socket
from time import sleep

while 1:
  s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
  s.sendto('helloworld', '10.8.0.1')
  sleep(2)