
import ecg_lib as ecgread
import ecg_processing as ecgprocess
import time
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import splrep, splev
from scipy.signal import detrend
import tools as st
from scipy.signal import butter, lfilter, freqz,cheby2,sosfilt,lfilter_zi
from hrcalc import PeakFinder


rawarray=[]
filteredarray=[]
peaksarray=[]
rpeaks_array=[]
number_read=1
edr_array=[]
rri_array=[]
e=ecgread.ECG()
sampling_rate=300
rri_interp_array=[]
hr_array=[]
num_values = 12
div_four = int(num_values/4)
window = 60/num_values

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
    interval = time_rri[-1]/num_values
    time_rri_interp = np.arange(0, time_rri[-1], interval)
    print("time_rri: ", time_rri)
    print("rri: ",rri)
    tck = splrep(time_rri, rri, s=0)
    rri_interp = splev(time_rri_interp, tck, der=0)
    return rri_interp, 1/interval



rawarray=[]
filteredarray=[]
peaksarray=[]
rpeaks_array=[0,0,0,0,0,0]
number_read=1
edr_array=[]
hr_array=[]
rpeaks_arrayu=[]
rri_interp_array=[]
filteredinside=[]
xaxis=range(0,1500)
#e=ecgread.ECG()
t=0
while True:
    print(len(edr_array))
    if len(edr_array)>10*5:
        break
    ecgraw=[]
    hr=[0]*5
    for i in range(300):
        output = e.analogInput(0)
        ecgraw.append(output)
        time.sleep(0.00333)
    filtered_butter=e.realtime_butter(ecgraw,35,0,300,5)
    t+=1
    outputarray=filtered_butter.tolist()
    filteredarray.extend(filtered_butter)
    rawarray.extend(ecgraw)
    if len(filteredarray)>1200:
          print(len(rawarray))
          ts,filtered,rpeaks=ecgprocess.ecg(rawarray[-1500:], 300, False,corr_rpeaks=True,calc_heartrate=False)
          print(len(filtered))
          print("rpeaks inside: {}".format(type(rpeaks[0])))
          #plt.figure()
          #plt.plot(xaxis,filtered)
          #plt.plot(rpeaks, filtered[rpeaks], 'o')
          #plt.title('ECG signal')
          #plt.xlabel('Samples')
          #_ =plt.ylabel('Voltage')
          #plt.show()
          filteredinside.extend(filtered[-300:])
          rpeaks=rpeaks+300*(number_read-1)
          rpeaks=(rpeaks/sampling_rate)*1000
          count = 0
          for i in range(0,len(rpeaks)):
                if rpeaks[i] not in rpeaks_array:
                      rpeaks_array.append(rpeaks[i])
                      rpeaks_arrayu.append(rpeaks[i])
                      count += 1
                     # print(rpeaks_array)
          rri = np.diff(rpeaks_array[-(count+1):])
          rri_array.extend(rri)
          rri_interp, dist = interp_cubic_spline(rri_array[-5:],4)
          print("last five: ", rri_array[-5:])
          print("rri interp:", rri_interp)
          print("last five length: ", len(rri_array[-5:]))
          print("rri interp length:", len(rri_interp))
          #print(len(rri_interp))
          if len(rri_interp_array)>=num_values:
              rri_interp_array.extend(rri_interp[-div_four:])
              for i in range(1, div_four+1):
                  hr[div_four-i] = 1000*(60/rri_interp_array[-i])
              #hr=1000*(60/rri_interp_array[-5:])
              hr_array.extend(hr)
              edr = detrend(hr)
              edr = (edr - edr.mean()) / edr.std()
              edr_array.extend(edr)
              number_read+=1
          else:
              rri_interp_array.extend(rri_interp)
              for i in range(1, div_four+1):
                  hr[div_four-i] = 1000*(60/rri_interp_array[-i])
              hr_array.extend(hr)
              edr = detrend(hr)
              edr = (edr - edr.mean()) / edr.std()
              edr_array.extend(edr)
              number_read+=1
# Find respiratory peaks
resp_peaks = PeakFinder.get(edr_array)
# Convert to seconds
resp_peaks = resp_peaks
rr = len(resp_peaks)*60/t
print("respiration rate: {}".format(rr))
plt.figure()
plt.plot(edr_array)
plt.show()
