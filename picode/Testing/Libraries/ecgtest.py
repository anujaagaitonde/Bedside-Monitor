# Importing modules
import spidev # To communicate with SPI devices
from numpy import interp	# To scale values
from time import sleep	# To add delay
import RPi.GPIO as GPIO	# To use GPIO pins

# Start SPI connection
spi = spidev.SpiDev() # Created an object
spi.open(0,0)	

# Read MCP3008 data
def analogInput(channel):
  spi.max_speed_hz = 1350000
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data

# Below function will convert data to voltage
def Volts(data):
  volts = (data * 3.3) / float(1023)
  volts = round(volts, 5) # Round off to 2 decimal places
  return volts


while True:
    output = analogInput(0)
    #ecg =  Volts(output)
    print(str(output))
    sleep(0.01)
