from pytun import TunTapDevice, IFF_TAP
from time import sleep

tap = TunTapDevice(name='tap0', flags=IFF_TAP)
tap.mtu = 1280

string = 'testing'

while 1:
  tap.write(string)
  sleep(2)