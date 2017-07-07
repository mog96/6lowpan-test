import socket
from time import sleep

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while 1:
  s.sendto('helloworld', ('127.0.0.1', 4901))
  sleep(2)