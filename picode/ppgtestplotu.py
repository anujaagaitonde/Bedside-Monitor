# Importing modules

from numpy import interp	# To scale values
from time import sleep	# To add delay

import matplotlib.pyplot as plt
from scipy.signal import detrend
import max30102_copy as max30102
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


# Parameters
x_len = 400         # Number of points to display
y_range = [26000, 28000]  # Range of possible Y values to display



# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = list(range(0, 400))
ys = [400] * x_len
ax.set_ylim(y_range)

#print(xs)
#print(ys)
# Create a blank line. We will update the line in animate
line, = ax.plot(xs, ys)

# Add labels
plt.title('PPG')
plt.xlabel('Samples')
#plt.ylabel('Volts (V)')


  
#plt.ion()
ppgarray=[]
filteredarray=[]
filtered_butterarray=[]
edr=[]
#x1=0
#x2=900
m=max30102.MAX30102()
nread=100
# This function is called periodically from FuncAnimation
def animate(i, ys):
    global x
    ecgarray=[]
    red, ir = m.read_sequential(nread)
    filtered_butter=realtime_butter(ir,40,2.50,100,1)
    #ts,filtered, rpeaks, templates_ts , templates ,heart_rate_ts , heart_rate = ecg(ecgarray, 300, False)
    ys.extend(red)
    #ys.append(math.sin(x/2*math.pi)) 

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
  
