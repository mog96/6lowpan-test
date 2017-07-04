from periphery import SPI
from time import sleep

while True:
  # Open spidev1.0 with mode 0 and max speed 1MHz
  spi = SPI("/dev/spidev0.0", 0, 400000)

  data_out = [0x00, 0x00, 0x00, 0x00]
  data_in = spi.transfer(data_out)

  print("shifted out [0x%02x, 0x%02x, 0x%02x, 0x%02x]" % tuple(data_out))
  print("shifted in  [0x%02x, 0x%02x, 0x%02x, 0x%02x]" % tuple(data_in))

  # sleep(1/400000)