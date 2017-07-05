from pytun import TunTapDevice, IFF_TAP

tap = TunTapDevice(name='tap0', flags=IFF_TAP)

while 1:
  print "swag",