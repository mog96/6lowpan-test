from pytun import TunTapDevice, IFF_TAP

tap = TunTapDevice(flags=IFF_TAP)
tap.name = 'tap0'
print tap.name