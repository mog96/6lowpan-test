from pytun import TunTapDevice, IFF_TAP
from time import sleep

tap = TunTapDevice(name='tap0', flags=IFF_TAP)
tap.mtu = 1280

tap.up()

test = buffer(1, 2, 3)

while 1:
  tap.write(s)
  sleep(2)