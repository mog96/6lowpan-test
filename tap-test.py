from pytun import TunTapDevice, IFF_TAP
from time import sleep

tap = TunTapDevice(name='tap0', flags=IFF_TAP)
tap.mtu = 1280

tap.up()

test = buffer('a', 'b', 'c')

while 1:
  tap.write(test)
  sleep(2)