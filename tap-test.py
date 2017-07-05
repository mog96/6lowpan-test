from pytun import TunTapDevice, IFF_TAP
from time import sleep

tap = TunTapDevice(name='tap0', flags=IFF_TAP)
tap.mtu = 1280

tap.up()

while 1:
  test = b"test"
  tap.write(test)
  sleep(2)