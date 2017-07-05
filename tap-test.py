from pytun import TunTapDevice, IFF_TAP

tap = TunTapDevice(name='tap0', flags=IFF_TAP)
print tap.name