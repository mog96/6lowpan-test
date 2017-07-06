from pytun import TunTapDevice, IFF_TAP
from time import sleep

tap = TunTapDevice(name='tap0', flags=IFF_TAP)
tap.addr = '10.8.0.1' # 'fa:ca:a9:29:69:61:65:3b'
tap.dstaddr = '10.8.0.2'
tap.netmask = '255.255.255.0'
tap.mtu = 1280

tap.up()

test = ''

while 1:
  buf = tap.read(tap.mtu)

  print buf

  tap.write(buf)