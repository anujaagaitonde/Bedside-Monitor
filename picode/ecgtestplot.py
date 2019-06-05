# Importing modules
import spidev # To communicate with SPI devices
from numpy import interp	# To scale values
from time import sleep	# To add delay
import RPi.GPIO as GPIO	# To use GPIO pins
import matplotlib.pyplot as plt
from scipy.signal import detrend
from ecg_processing import ecg
from scipy.interpolate import splrep, splev, interp1d
import numpy as np


# Start SPI connection
spi = spidev.SpiDev() # Created an object
spi.open(0,0)	
spi.max_speed_hz = 1350000

# Read MCP3008 data
def analogInput(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data

# Below function will convert data to voltage
def Volts(data):
  volts = (data * 3.3) / float(1023)
  volts = round(volts, 5) # Round off to 2 decimal places
  return volts



# Interpolate and compute HR
def calcresp(ecgarray,rpeaks):
    ecgarray = np.asarray(ecgarray)
    f = interp1d(rpeaks,ecgarray[rpeaks], kind='linear')
    rpeaks_interp = np.arange(rpeaks[0], rpeaks[-1]+1)
    edr = f(rpeaks_interp)
    edr -=np.mean(edr)
    return edr
plt.ion()
ecgarray=[]
filteredarray=[]
edr=[]
x1=0
x2=900
while True:
    #ecgarray=[]
  for j in range(1):
    for i in range(900):
      output = analogInput(0)
      ecgarray.append(output)
      sleep(0.00333)
    ts,filtered, rpeaks, templates_ts , templates ,heart_rate_ts , heart_rate = ecg(ecgarray, 300, False)
    print(np.mean(heart_rate))
    #edr.extend(calcresp(filtered,rpeaks))
    filteredarray.extend(filtered)
    axes=plt.gca()
    axes.set_xlim([x1,x2])
    plt.plot(filteredarray)
    #plt.plot(ecgarray)
    plt.draw()
    plt.pause(0.0003)
  x1=x1+900
  x2=x2+900
