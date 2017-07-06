from pytun import TunTapDevice, IFF_TAP
from time import sleep

tap = TunTapDevice(name='tap0', flags=IFF_TAP)
tap.addr = '10.8.0.1'
tap.dstaddr = '10.8.0.2'
tap.netmask = '255.255.255.0'
tap.mtu = 1280

tap.up()

test = ''

while 1:
  test = 'test'
  # tap.write(test)
  sleep(2)