import numpy as np

import matplotlib.pyplot as plt

from scipy.interpolate import splrep, splev

from scipy.signal import detrend
import tools as st
import ecg_lib as ecg
from scipy.signal import butter, lfilter, freqz,cheby2,sosfilt,lfilter_zi

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

def Volts(data):
  volts = (data * 3.3) / float(1023)
  volts = round(volts, 5) # Round off to 2 decimal places
  return volts

def interp_cubic_spline(rri, sf_up=4):
    """
    Interpolate R-R intervals using cubic spline.
    Taken from the `hrv` python package by Rhenan Bartels.

    Parameters
    ----------
    rri : np.array
        R-R peak interval (in ms)
    sf_up : float
        Upsampling frequency.

    Returns
    -------
    rri_interp : np.array
        Upsampled/interpolated R-R peak interval array
    """
    rri_time = np.cumsum(rri) / 1000.0
    time_rri = rri_time - rri_time[0]
    time_rri_interp = np.arange(0, time_rri[-1], 1 / float(sf_up))
    #print(time_rri)
    #print(rri)
    tck = splrep(time_rri, rri, s=0)
    rri_interp = splev(time_rri_interp, tck, der=0)
    return rri_interp


# Load and preprocess data
ecgarray=np.genfromtxt('ecg_data.csv',delimiter=',')
sampling_rate=300

plt.figure()
plt.plot(ecgarray)
plt.show()
for i in range(1,len(ecgarray)):
    ecgarray[i]=Volts(ecgarray[i])


filtered_array=[]
rpeaks_array=[]
ts_array=[]
rri_array=[]
rri_interp_array=[]
hr_array=[]
edr_array=[]

ts,filtered, rpeaks= ecg.ecg(ecgarray[:1500], 300.0, False,corr_rpeaks=True,calc_heartrate=False)
#filtered=filtered_butter=realtime_butter(ecgarray[:2100],43,3,300.,5)
#rpeaks= ecg.hamilton_segmenter(filtered[60:])
rpeaks=np.asarray(rpeaks)
print(rpeaks)
xaxis=range(0,1500)
# R-R peaks detection
#rr, _ = find_peaks(ecg, distance=40, height=0.5)
plt.figure()
plt.plot(xaxis,filtered)
plt.plot(rpeaks, filtered[rpeaks], 'o')
plt.title('ECG signal')
plt.xlabel('Samples')
_ =plt.ylabel('Voltage')
#plt.show()

#rpeaks_array.extend(rpeaks)
filtered_array.extend(filtered)
#ts_array.extend(ts)
rpeaks = (rpeaks / sampling_rate) * 1000
rpeaks_array.extend(rpeaks)
print(rpeaks)
rri = np.diff(rpeaks)
rri_array.extend(rri)
print(rri_array)
#print(rri)
rri_interp = interp_cubic_spline(rri,4)
rri_interp_array.extend(rri_interp)
hr=1000*(60/rri_interp)
hr_array.extend(hr)
edr = detrend(hr)
m=1200
adjust=401
print("First Done")


plt.figure()
for j in range(1,7):
    print(j)
    #filtered=filtered_butter=realtime_butter(ecgarray[m:m+800],43,3,300.,5)
    #rpeaks= ecg.hamilton_segmenter(filtered)
    xaxis=range(m,m+900)
    ts,filtered, rpeaks= ecg.ecg(ecgarray[m:m+900], 300, False,corr_rpeaks=True,calc_heartrate=False)
    #print(rpeaks)
    rpeaks= rpeaks+(1200)+adjust*(j-1)
    print(rpeaks)
    #plt.plot(xaxis,filtered)
    #plt.plot(rpeaks, filtered[rpeaks], 'o')
    #plt.show()
    #print(filtered)
    #filtered_array.extend(filtered)
    #ts_array.extend(ts)
    #rpeaks= rpeaks+(2000)+adjust*(j-1)
    rpeaks = (rpeaks / sampling_rate) * 1000
    print(rpeaks)
    for i in range(0,len(rpeaks)):
        if rpeaks[i] not in rpeaks_array:
            rpeaks_array.append(rpeaks[i])
    print(rpeaks_array)
    rri = np.diff(rpeaks_array[-4:])
    rri_array.extend(rri)
    print(rri_array)
    rri_interp = interp_cubic_spline(rri_array,4)
    rri_interp_array.extend(rri_interp)
    hr=1000*(60/rri_interp)
    hr_array.extend(hr)
    edr = detrend(hr)
    edr = (edr - edr.mean()) / edr.std()
    edr_array.extend(edr)
    m+=601
    adjust=601

plt.figure()
plt.plot(edr)
#plt.show()






ts,filtered, rpeaks= ecg.ecg(ecgarray, 300, False,corr_rpeaks=True,calc_heartrate=False)
#ecg = filter_data(ecg, sf_ori, 3, 45, verbose=0)

'''
# Select only a 10 sec window
wind = 5
start = 600
ecg = ecg[int(start*sf):int((start+wind)*sf)]
'''

# R-R peaks detection
#rr, _ = find_peaks(ecg, distance=40, height=0.5)
plt.figure()
plt.plot(filtered)
plt.plot(rpeaks, filtered[rpeaks], 'o')
plt.title('ECG signal')
plt.xlabel('Samples')
_ =plt.ylabel('Voltage')
#plt.show()

# R-R interval in ms
rpeaks = (rpeaks / sampling_rate) * 1000
rri = np.diff(rpeaks)
print(rpeaks)
print(rri)
sf_up = 4
rri_interp = interp_cubic_spline(rri,4)
hr = 1000 * (60 / rri_interp)


# Detrend and normalize
edr = detrend(hr)
edr = (edr - edr.mean()) / edr.std()
'''
#print (edr)
# Find respiratory peaks
resp_peaks, _ = find_peaks(edr, height=0, distance=sf_up)

# Convert to seconds
resp_peaks = resp_peaks
resp_peaks_diff = np.diff(resp_peaks) / sf_up
'''
# Plot the EDR waveform
plt.figure()
plt.plot(edr, '-')
#plt.plot(resp_peaks, edr[resp_peaks], 'o')
_ = plt.title('ECG derived respiration')
plt.show()

