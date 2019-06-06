# Importing modules
import spidev # To communicate with SPI devices
from numpy import interp	# To scale values
from time import sleep	# To add delay
import RPi.GPIO as GPIO	# To use GPIO pins
import matplotlib.pyplot as plt
from scipy.signal import detrend
from ecg_processing import ecg
from scipy.interpolate import splrep, splev, interp1d
from scipy.signal import butter, lfilter, freqz,cheby2,sosfilt,lfilter_zi
import numpy as np
import matplotlib.animation as animation
import threading


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


# Start SPI connection
spi = spidev.SpiDev() # Created an object
spi.open(0,0)	
spi.max_speed_hz = 1350000

x_len = 400         # Number of points to display
y_range = [400, 700] 

filteredecgarray=[]



class ECGThread (threading.Thread):
    global filteredecgarray
    def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
    def run(self):
       # Start SPI connection
       spi = spidev.SpiDev() # Created an object
       spi.open(0,0)
       spi.max_speed_hz = 1350000
       ecgarray=[]
       print ("Starting " + self.name)       
       while True:
           for i in range(300):
                output = analogInput(0)
                ecgarray.append(output)
                sleep(0.00333)
           ecgarray=ecgarray[-900:]
           filtered_butter=realtime_butter(ecgarray,35,0,300,5)
           
           filteredecgarray.extend(filtered_butter)
       #print_time(self.name, 5, self.counter)
       print ("Exiting " + self.name)


# Read MCP3008 data
def analogInput(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data


class GUIThread (threading.Thread):
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
   def run(self):
      sleep(3)
      print ("Starting " + self.name)
      # Parameters
      # Range of possible Y values to display
      # Create figure for plotting
      fig = plt.figure()
      ax = fig.add_subplot(1, 1, 1)
      xs = list(range(0, 400))
      ys = [550] * x_len
      ax.set_ylim(y_range)
      self.line, = ax.plot(xs, ys)
      print("GUIThread")
      print("GUI Initilised")
      ani=animation.FuncAnimation(fig,self.animate,fargs=(ys,),interval=1,blit=True)
      plt.show()
      #print_time(self.name, 5, self.counter)
      print ("Exiting " + self.name)
   def animate(self,i, ys):
      #sleep(0.00333)
      ys.append(filteredecgarray.pop()) 
      # Add y to list
      #ys.append(temp_c)
      '''
      x += 1
      if (x/(2*math.pi))==1:
          x=0
      '''
      # Limit y list to set number of items
      ys = ys[-x_len:]
      # Update line with new Y values
      self.line.set_ydata(ys)
      return self.line,

thread1 = GUIThread(1, "GUIThread")
thread2 = ECGThread(2, "ECGThread")

thread1.start()
thread2.start()

