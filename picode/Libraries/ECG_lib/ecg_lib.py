# Importing modules
import spidev # To communicate with SPI devices
from numpy import interp	# To scale values
from time import sleep	# To add delay
import RPi.GPIO as GPIO	# To use GPIO pins
from scipy.signal import detrend
import ecg_processing
from scipy.interpolate import splrep, splev, interp1d
import numpy as np
from scipy.signal import butter, lfilter, freqz,cheby2,sosfilt,lfilter_zi

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
        for i in range(sec):
            output = self.analogInput(0)
            ecgarray.append(output)
            sleep(1/sample_rate)
        return ecgarray
    def butter_bandpass(self,lowcut, highcut, fs, order=1):
        '''
        This function calculates butter bandpass
        '''
        nyq = 0.5 * fs
        low = lowcut / nyq
        high = highcut / nyq
        #print(low)
        #print(high)
        b, a = butter(order, low, btype='lowpass')
        return b, a
      
    def realtime_butter(self,data,lowcut,highcut,fs,order=1):
        b, a = self.butter_bandpass(lowcut, highcut, fs, order=order)
        zi=lfilter_zi(b,a)
        y,zf= lfilter(b,a,data,zi=zi*data[0])
        return y

    #filters array of data returning filtered signal, heart rate and rpeaks
    def filter(data,sample_rate,show=False):
        ts,filtered, rpeaks, templates_ts , templates ,heart_rate_ts , heart_rate = ecg_processing.ecg(ecgarray, 300, False)
        return ts,filtered, rpeaks, templates_ts , templates ,heart_rate_ts , heart_rate
    
