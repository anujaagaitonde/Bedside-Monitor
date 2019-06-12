
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

def get_respiration(ecgraw,sampling_rate,count,lastPeak=None):
    if lastPeak:
        rpeaks_array = [lastPeak]
    else:
        rpeaks_array = []
    ts,filtered,rpeaks=ecgprocess.ecg(ecgraw, 300, False,corr_rpeaks=True,calc_heartrate=False)
    rpeaks=rpeaks+300*(count)
    rpeaks=(rpeaks/sampling_rate)*1000
    rpeaks_array.extend(rpeaks)
    rri = np.diff(rpeaks_array)
    rri_interp = interp_cubic_spline(rri,4)
    hr=1000*(60/rri_interp)
    edr = detrend(hr)
    edr = (edr - edr.mean()) / edr.std()
    heart_rate = int(len(rpeaks)*60/(len(ecgraw)/sampling_rate))
    return edr,heart_rate,count+1,rpeaks_array[-1]

def get_rr(edr,time_interval):
    resp_peaks=PeakFinder.get(edr)
    rr=len(resp_peaks)*60/time_interval
    return rr
