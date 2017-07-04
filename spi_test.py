from periphery import SPI
from time import sleep

with open("log.txt", 'w') as f:
  while True:
    # Open spidev1.0 with mode 0 and max speed 1MHz
    spi = SPI("/dev/spidev0.0", 0, 400000)

    data_out = [0x00, 0x00, 0x00, 0x00]
    data_in = spi.transfer(data_out)

    # print("[0x%02x, 0x%02x, 0x%02x, 0x%02x]" % tuple(data_out))
    f.write("[0x%02x, 0x%02x, 0x%02x, 0x%02x]" % tuple(data_in) + '\n')

    # sleep(1/400000)