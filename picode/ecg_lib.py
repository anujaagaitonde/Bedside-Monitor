# Importing modules
import spidev # To communicate with SPI devices
from numpy import interp	# To scale values
from time import sleep	# To add delay
import RPi.GPIO as GPIO	# To use GPIO pins
from scipy.signal import detrend
from ecg_processing import ecg
from scipy.interpolate import splrep, splev, interp1d
import numpy as np

# Start SPI connection
spi = spidev.SpiDev() # Created an object
spi.open(0,0)	


class ECG():
    #Opening spi comm
    def __init__(self):
        self.spi=spidev.SpiDev()
        self.spi.open(0,0)
        self.spi.max_speed_hz= 1350000
    #reading from MCP3008 returns 1 data sample
    def analogInput(self,channel):
        spi.max_speed_hz = 1350000
        adc = spi.xfer2([1,(8+channel)<<4,0])
        data = ((adc[1]&3) << 8) + adc[2]
        return data
    #Reading an array of samples from MCP3008 returns array
    def read_store(self,sample_rate,sec):
        ecgarray=[]
        for i in range(900):
            output = self.analogInput(0)
            ecgarray.append(output)
            sleep(1/sample_rate)
        return ecgarray
    #filters array of data returning filtered signal, heart rate and rpeaks
    def filter(data,sample_rate,show=False):
        ts,filtered, rpeaks, templates_ts , templates ,heart_rate_ts , heart_rate = ecg(ecgarray, 300, False)
        return ts,filtered, rpeaks, templates_ts , templates ,heart_rate_ts , heart_rate
    
