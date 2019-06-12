
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
    time_rri_interp = np.arange(0, time_rri[-1], 1 / float(sf_up))
    #print(time_rri)
    #print(rri)
    tck = splrep(time_rri, rri, s=0)
    rri_interp = splev(time_rri_interp, tck, der=0)
    return rri_interp
number_read=1

while True:
    ecgraw=[]
    for i in range(1500):
        output = e.analogInput(0)
        ecgraw.append(output)
        time.sleep(0.00333)
    ts,filtered,rpeaks=ecgprocess.ecg(ecgraw, 300, False,corr_rpeaks=True,calc_heartrate=False)
    rpeaks=rpeaks+300*(number_read-1)
    number_read+=1
    rpeaks=(rpeaks/sampling_rate)*1000
    rpeaks_array.extend(rpeaks)
    rri = np.diff(rpeaks)
    rri_array.extend(rri)
    print(rri_array)
    rri_interp = interp_cubic_spline(rri,4)
    rri_interp_array.extend(rri_interp)
    hr=1000*(60/rri_interp)
    hr_array.extend(hr)
    edr = detrend(hr)
    edr = (edr - edr.mean()) / edr.std()
    edr_array.extend(edr)
    resp_peaks=PeakFinder.get(edr)
    rr=len(resp_peaks)*12
    print("Respiration Rate: {}".format(rr))
    rpeaks_array = rpeaks_array[-1:]
    plt.figure()
    plt.plot(edr)
    plt.show()


