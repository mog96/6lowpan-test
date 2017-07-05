from pytun import TunTapDevice, IFF_TAP

tap = TunTapDevice(name='tap0', flags=IFF_TAP)
tun.addr = '10.8.0.1'
tun.dstaddr = '10.8.0.2'
tun.netmask = '255.255.255.0'
tap.mtu = 1280

while 1:
  print "swag",