from pytun import TunTapDevice, IFF_TAP

tap = TunTapDevice(name='tap0', flags=IFF_TAP)
print tap.name
print tap.addr
print tap.dstaddr
print tap.netmask
print tap.mtu