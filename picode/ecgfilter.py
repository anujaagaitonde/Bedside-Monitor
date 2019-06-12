# Importing modules
#import spidev # To communicate with SPI devices
from numpy import interp	# To scale values
from time import sleep	# To add delay
#import RPi.GPIO as GPIO	# To use GPIO pins
import matplotlib.pyplot as plt
from scipy.signal import detrend
#from ecg_processing import ecg
from scipy.interpolate import splrep, splev, interp1d
from scipy.signal import butter, lfilter, freqz,cheby2,sosfilt,lfilter_zi
import numpy as np
import matplotlib.animation as animation



# Interpolate and compute HR
def calcresp(ecgarray,rpeaks):
    ecgarray = np.asarray(ecgarray)
    f = interp1d(rpeaks,ecgarray[rpeaks], kind='linear')
    rpeaks_interp = np.arange(rpeaks[0], rpeaks[-1]+1)
    edr = f(rpeaks_interp)
    edr -=np.mean(edr)
    return edr

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

# Parameters
x_len = 900         # Number of points to display
y_range = [350, 650]  # Range of possible Y values to display

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = list(range(0, 400))
ys = [550] * x_len
ax.set_ylim(y_range)
line, = ax.plot(xs, ys)
ecgarray=np.genfromtxt('ecg_data.csv',delimiter=',')
index=0
def animate(i, ys):
    global x
    #ecgarray2=np.asarray(ecgarray)
    #np.savetxt("ecg_data.csv",ecgarray2,delimiter=",")
    #print("Done")
    #filtered_butter=realtime_butter(ecgarray,35,0,300,5)
    #ts,filtered, rpeaks, templates_ts , templates ,heart_rate_ts , heart_rate = ecg(ecgarray, 300, False)
    #ys.extend(filtered_butter)
    ys.append(ecgarray[i])
    i+=1
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
    line.set_ydata(ys)
    return line,
# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig,
    animate,
    fargs=(ys,),
    interval=1,
    blit=True)
plt.show()
