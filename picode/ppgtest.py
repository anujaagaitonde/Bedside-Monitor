from numpy import interp	# To scale values
from time import sleep	# To add delay

import matplotlib.pyplot as plt
from scipy.signal import detrend
import max30102_doug as max30102
from scipy.signal import butter, lfilter, freqz,cheby2,sosfilt,lfilter_zi
import numpy as np
import matplotlib.animation as animation

def butter_bandpass(lowcut, highcut, fs, order=1):
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
  
def realtime_butter(data,lowcut,highcut,fs,order=1):
  b, a = butter_bandpass(lowcut, highcut, fs, order=order)
  zi=lfilter_zi(b,a)
  y,zf= lfilter(b,a,data,zi=zi*data[0])
  return y



m=max30102.MAX30102()
nread=100

while True:
    red,ir=m.read_sequential(nread)
    print(ir)
