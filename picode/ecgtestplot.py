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

# Interpolate and compute HR
def calcresp(ecgarray,rpeaks):
    ecgarray = np.asarray(ecgarray)
    f = interp1d(rpeaks,ecgarray[rpeaks], kind='linear')
    rpeaks_interp = np.arange(rpeaks[0], rpeaks[-1]+1)
    edr = f(rpeaks_interp)
    edr -=np.mean(edr)
    return edr

# Parameters
x_len = 400         # Number of points to display
y_range = [350, 650]  # Range of possible Y values to display



# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = list(range(0, 400))
ys = [550] * x_len
ax.set_ylim(y_range)

#print(xs)
#print(ys)
# Create a blank line. We will update the line in animate
line, = ax.plot(xs, ys)

# Add labels
plt.title('ECG')
plt.xlabel('Samples')
plt.ylabel('Volts (V)')


  
#plt.ion()
ecgarray=[]
filteredarray=[]
filtered_butterarray=[]
edr=[]
#x1=0
#x2=900

# This function is called periodically from FuncAnimation
def animate(i, ys):
    global x
    ecgarray=[]
    for i in range(6000):
    # Read temperature (Celsius) from TMP102
    #temp_c = round(tmp102.read_temp(), 2)
    #for i in range(100):
      output = analogInput(0)
      ecgarray.append(output)
      sleep(0.00333)
    ecgarray2=np.asarray(ecgarray)
    np.savetxt("ecg_data.csv",ecgarray2,delimiter=",")
    print("Done")
    filtered_butter=realtime_butter(ecgarray,35,0,300,5)
    #ts,filtered, rpeaks, templates_ts , templates ,heart_rate_ts , heart_rate = ecg(ecgarray, 300, False)
    ys.extend(filtered_butter)
    ecgarray
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
  
'''
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
    filtered_butter=realtime_butter(ecgarray,40,0,300,5)
    filtered_butterarray.extend(filtered_butter)
    filteredarray.extend(filtered)
    axes=plt.gca()
    axes.set_xlim([x1,x2])
    #plt.plot(filtered)
    plt.plot(filtered_butterarray)
    plt.plot(ecgarray)
    plt.draw()
    plt.pause(0.0003)
  x1=x1+900
  x2=x2+900
'''
