#-----------------------------------------------------------------------------
# CS 244 Assignment 8
# Jiawei Chiang (jiawec5)
# This script was co-written by Team 20 members.
#
# Creation Date : Sat 2 Dec 2017 11:34:39 PM PDT
# Last Modified : Sat 3 Dec 2017 01:20:20 AM PDT
#----------------------------------------------------------------------------- 

import numpy as np
from scipy.signal import butter, lfilter, freqz,cheby2,sosfilt
import matplotlib.pyplot as plt
import scipy as sc
from scipy.interpolate import interp1d
import pandas as pd
import math
from decimal import *
from numpy import atleast_2d as twod
#from sklearn.svm import SVC
#import xlrd

def butter_bandpass(lowcut, highcut, fs, order=1):
    '''
    This function calculates butter bandpass
    '''
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    print(low)
    print(high)
    b, a = butter(order, low, btype='lowpass')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=1):
    '''
    This function constructs bandpass filtered signal
    '''
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

def ChebyshevII(data, lowcut, highcut, fs, order=4,attenuation=20):
    '''  This function constucts a Chebyshev type 2 filter and returns a filtered output '''
    fn=fs/2
    nlowcut=(lowcut/fn)
    nhighcut=(highcut/fn)
    parameters=cheby2(order,attenuation,[nlowcut, nhighcut],btype="bandpass",analog=True,output='sos')
    output=sosfilt(parameters,data)
    return output

def calculate_HR(IR, lowcut, highcut, fs=100.0, order=5):
    '''
    This function calculates real-time heart rate from given IR readings
    '''
    #dataset_HR = butter_bandpass_filter(IR, lowcut, highcut, fs, order=order) #1.1, 2.0, 5
    dataset_HR= ChebyshevII(IR,lowcut,highcut,fs,order=order)
    #hrw1 = 0.05 #One-sided window size, as proportion of the sampling frequency
    #dataset_HR = pd.rolling_mean(dataset_HR, window=int(hrw1*fs)) #Calculate moving average
    #plt.figure()
    #plt.plot(dataset_HR)
    #plt.title("ChebyshevII output of IR Signal order=4 for HR\n ")
    #plt.savefig('figures/Figure01.png')
    #plt.show()

    #Calculate moving average with 0.75s in both directions, then append do dataset
    hrw = 0.75 #One-sided window size, as proportion of the sampling frequency
    mov_avg = pd.rolling_mean(dataset_HR, window=int(hrw*fs)) #Calculate moving average
    #Impute where moving average function returns NaN, which is the beginning of the signal where x hrw
    avg_hr = (np.mean(dataset_HR))
    mov_avg = [avg_hr if math.isnan(x) else x for x in mov_avg]
    mov_avg = [x*1.0002 for x in mov_avg] #For now we raise the average by 20% to prevent the secondary heart contraction from interfering, in part 2 we will do this dynamically
    hart_rollingmean = mov_avg #Append the moving average to the dataframe
    #Mark regions of interest
    window = []
    peaklist = []
    newpeaklist = []
    newybeat = []
    listpos = 0 #We use a counter to move over the different data columns
    for datapoint in dataset_HR:
        rollingmean = hart_rollingmean[listpos] #Get local mean
        if (datapoint < rollingmean) and (len(window) < 1): #If no detectable R-complex activity -> do nothing
            listpos += 1

        elif (datapoint > rollingmean): #If signal comes above local mean, mark ROI
            window.append(datapoint)
            listpos += 1
            
        else: #If signal drops below local mean -> determine highest point
            maximum = max(window)
            beatposition = listpos - len(window) + (window.index(max(window))) #Notate the position of the point on the X-axis
            peaklist.append(beatposition) #Add detected peak to list
            window = [] #Clear marked ROI
            listpos += 1
    ybeat = [dataset_HR[x] for x in peaklist] #Get the y-value of all peaks for plotting purposes

    for i in range(len(peaklist)):
        if (peaklist[i]>100):
            newpeaklist.append(peaklist[i])
            newybeat.append(ybeat[i])
    
    #plt.figure()
    #plt.title("Detected Peaks in IR Signal for Heart Rate")
##    #plt.xlim(2600,2800)
##    plt.ylim(-600,600)
    #plt.plot(dataset_HR, alpha=0.5, color='blue') #Plot semi-transparent HR
    #plt.plot(mov_avg, color ='green') #Plot moving average
    #plt.scatter(newpeaklist, newybeat, color='red') #Plot detected peaks
    #plt.savefig('figures/Figure02.png')
    #plt.show()

    hr_interval= []
    cnt = 0
    heart_rate = []
    while (cnt < (len(newpeaklist)-1)):
        RR_interval = (newpeaklist[cnt+1] - newpeaklist[cnt]) #Calculate distance between beats in # of samples
        ms_dist = ((1.0*RR_interval / fs) * 1000.0) #Convert sample distances to ms distances
        hr_interval.append(ms_dist) #Append to list
        cnt += 1
    for i in range(len(hr_interval)):
        heart_rate.append(60000/hr_interval[i])
    
    print('heart rate (beats/min) = ',heart_rate)
    #hr_peaktime = [time[x] for x in newpeaklist] # peak time for heart rate
    #plt.figure()
    #plt.plot(heart_rate)
    #plt.title("Plot of Heart Rate")
    #plt.xlabel("Peaks")
    #plt.ylabel("HR (beats/min)")
    #plt.savefig(netid+'_figures/'+netid+'_'+activity_name+'_HR.png')
    
    print("the mean of heart rate is {} beats/min.\n".format(np.mean(heart_rate)))
    #plt.show()
    return (heart_rate)


def calculate_RR(IR, lowcut, highcut, fs=100, order=5):
    '''
    This function calculates real-time respiration rate from given IR readings


    '''
    #plt.figure()
    #plt.plot(IR)
    #plt.title("IR Signal for RR")
    
    dataset_RR = butter_bandpass_filter(IR, lowcut, highcut, fs, order=order) # 0.210, 0.333, 5
    #dataset_RR=IR

    #plt.figure()
    #plt.plot(dataset_RR)
    #plt.title("Bandpass-Filtered 5th-Order IR Signal for RR")
    #plt.savefig('figures/Figure04.png')
    #plt.show()

    #Calculate moving average with 0.75s in both directions, then append do dataset
    hrw = 0.75  #One-sided window size, as proportion of the sampling frequency
    mov_avg = pd.rolling_mean(dataset_RR, window=int(hrw*fs))
    #Impute where moving average function returns NaN, which is the beginning of the signal where x hrw
    avg_hr = (np.mean(dataset_RR))
    mov_avg = [avg_hr if math.isnan(x) else x for x in mov_avg]
    
    mov_avg = [x*1.0004 for x in mov_avg] #For now we raise the average by 20% to prevent the secondary heart contraction from interfering, in part 2 we will do this dynamically
    hart_rollingmean = mov_avg #Append the moving average to the dataframe
    #Mark regions of interest
    window = []
    peaklist = []
    newpeaklist = []
    newybeat = []
    listpos = 0 #We use a counter to move over the different data columns
    for datapoint in dataset_RR:
        rollingmean = hart_rollingmean[listpos] #Get local mean
        if (datapoint < rollingmean) and (len(window) < 1): #If no detectable R-complex activity -> do nothing
            listpos += 1

        elif (datapoint > rollingmean): #If signal comes above local mean, mark ROI
            window.append(datapoint)
            listpos += 1
            
        else: #If signal drops below local mean -> determine highest point
            maximum = max(window)
            beatposition = listpos - len(window) + (window.index(max(window))) #Notate the position of the point on the X-axis
            peaklist.append(beatposition) #Add detected peak to list
            window = [] #Clear marked ROI
            listpos += 1
    ybeat = [dataset_RR[x] for x in peaklist] #Get the y-value of all peaks for plotting purposes
    #rr_peaktime = [time[x] for x in peaklist] # peak time for respiration rate
    rr_interval = []
    cnt = 0
    respiration_rate = []
    while (cnt < (len(peaklist)-1)):
        RR_interval = (peaklist[cnt+1] - peaklist[cnt]) #Calculate distance between beats in # of samples
        ms_dist = ((1.0*RR_interval / fs) * 1000.0) #Convert sample distances to ms distances
        rr_interval.append(ms_dist) #Append to list
        cnt += 1
    for i in range(len(rr_interval)):
        respiration_rate.append(60000/rr_interval[i])
    respiration_rate = respiration_rate[1:]
    #rr_peaktime = rr_peaktime[1:]
    print('respiration rate (breaths/min) = ',respiration_rate)

    #plt.figure()
    #plt.title("Detected Peaks in IR Signal for Respiration Rate ")
    #plt.plot(dataset_RR, alpha=0.5, color='blue') #Plot semi-transparent HR
    #plt.plot(mov_avg, color ='green') #Plot moving average
    #plt.scatter(peaklist, ybeat, color='red') #Plot detected peaks
    #plt.savefig('figures/Figure05.png')
    #plt.show()

    #plt.figure()
    #plt.plot(respiration_rate)
    #plt.title("Plot of Respiration Rate")
    #plt.xlabel("Peaks")
    #plt.ylabel("RR (breaths/min)")
 

    print("the mean of respiration rate is {} breaths/min.\n".format(np.mean(respiration_rate)))
    #plt.show()
    return (respiration_rate)


def calculate_SPO2(IR, RED, lc_ir, hc_ir, lc_red, hc_red, fs=50, order=5, pk_min = 1, pk_max = -1):

    #plt.figure()
    #plt.plot(IR)
    #plt.title("IR Signal for SPO2")

    #This function calculates real-time SPO2 from given IR and RED readings
    #plt.ion()
    dataset_IR = butter_bandpass_filter(IR, lc_ir, hc_ir, fs, order=order) #1.1, 2.2, 5
    #plt.figure()
    #plt.plot(dataset_IR)
    #plt.title("Bandpass-Filtered 5th-Order IR Signal for SPO2")
    #plt.savefig('figures/Figure07.png')
    #plt.show()

    #Calculate moving average with 3s in both directions, then append do dataset
    hrw = 0.75 #One-sidedwindow size, as proportion of the sampling frequency
    mov_avg = pd.rolling_mean(dataset_IR, window=int(hrw*fs)) #Calculate moving average

    #Impute where moving average function returns NaN, which is the beginning of the signal where x hrw
    avg_hr = (np.mean(dataset_IR))
    mov_avg = [avg_hr if math.isnan(x) else x for x in mov_avg]
    mov_avg = [x*1.0004 for x in mov_avg] #For now we raise the average by 20% to prevent the secondary heart contraction from interfering, in part 2 we will do this dynamically
    hart_rollingmean = mov_avg #Append the moving average to the dataframe
    #Mark regions of interest
    window = []
    peaklist = []
    newpeaklist = []
    IR_peak = []
    listpos = 0 #We use a counter to move over the different data columns
    for datapoint in dataset_IR:
        rollingmean = hart_rollingmean[listpos] #Get local mean
        if (datapoint < rollingmean) and (len(window) < 1): #If no detectable R-complex activity -> do nothing
            listpos += 1

        elif (datapoint > rollingmean): #If signal comes above local mean, mark ROI
            window.append(datapoint)
            listpos += 1
            
        else: #If signal drops below local mean -> determine highest point
            maximum = max(window)
            beatposition = listpos - len(window) + (window.index(max(window))) #Notate the position of the point on the X-axis
            #if (datapoint>150):
            peaklist.append(beatposition) #Add detected peak to list
            window = [] #Clear marked ROI
            listpos += 1
            
    IR_peak = [dataset_IR[x] for x in peaklist] 

    convertedIR = -dataset_IR; 

    #Calculate moving average with 3s in both directions, then append do dataset
    mov_avg = pd.rolling_mean(convertedIR, window=int(hrw*fs)) #Calculate moving average

    #Impute where moving average function returns NaN, which is the beginning of the signal where x hrw
    avg_hr = (np.mean(convertedIR))
    mov_avg = [avg_hr if math.isnan(x) else x for x in mov_avg]
    mov_avg = [x*1.0004 for x in mov_avg] #For now we raise the average by 20% to prevent the secondary heart contraction from interfering, in part 2 we will do this dynamically
    hart_rollingmean = mov_avg #Append the moving average to the dataframe
    #Mark regions of interest    
        
    minlist = []
    newvalleylist = []
    IR_min = []    
    window = []    
    listpos = 0    
    for datapoint in convertedIR:
        rollingmean = hart_rollingmean[listpos] #Get local mean
        if (datapoint < rollingmean) and (len(window) < 1): #If no detectable R-complex activity -> do nothing
            listpos += 1
        elif (datapoint > rollingmean): #If signal comes above local mean, mark ROI
            window.append(datapoint)
            listpos += 1
        else: #If signal drops below local mean -> determine highest point
            maximum = max(window)
            beatposition = listpos - len(window) + (window.index(max(window))) #Notate the position of the point on the X-axis
            #if (datapoint>150):
            minlist.append(beatposition) #Add detected peak to list
            window = [] #Clear marked ROI
            listpos += 1

    IR_min = [-convertedIR[x] for x in minlist] 

    num=len(IR_min)
    DC_IR=[]
    AC_IR=[]
    for i in range(1, num) :
        x=np.linspace(minlist[i-1], minlist[i])
        y=np.linspace(IR_min[i-1], IR_min[i])
        f=interp1d(x,y)
        DC_IR.append(f(peaklist[i]))
      
    for i in range(1, num) :
        AC_IR.append(IR_peak[i]-DC_IR[i-1])
        
    newpeaklist=peaklist[pk_min:pk_max]
    
    dataset_RED = butter_bandpass_filter(RED, lc_red, hc_red, fs, order=order) #1.1, 2.2, 5
    #plt.figure(1)
    #plt.plot(dataset_RED)
    #plt.title("Bandpass-Filtered 5th-Order RED Signal for SPO2")
    #plt.savefig('figures/Figure08.png')
    #plt.show()

    mov_avg = pd.rolling_mean(dataset_RED, window=int(hrw*fs)) #Calculate moving average

    #Impute where moving average function returns NaN, which is the beginning of the signal where x hrw
    avg_hr = (np.mean(dataset_RED))
    mov_avg = [avg_hr if math.isnan(x) else x for x in mov_avg]
    mov_avg = [x*1.0004 for x in mov_avg] #For now we raise the average by 20% to prevent the secondary heart contraction from interfering, in part 2 we will do this dynamically
    hart_rollingmean = mov_avg #Append the moving average to the dataframe
    #Mark regions of interest
    window = []
    RED_peaklist = []
    RED_newpeaklist = []
    RED_peak = []
    listpos = 0 #We use a counter to move over the different data columns
    for datapoint in dataset_RED:
        rollingmean = hart_rollingmean[listpos] #Get local mean
        if (datapoint < rollingmean) and (len(window) < 1): #If no detectable R-complex activity -> do nothing
            listpos += 1

        elif (datapoint > rollingmean): #If signal comes above local mean, mark ROI
            window.append(datapoint)
            listpos += 1
            
        else: #If signal drops below local mean -> determine highest point
            maximum = max(window)
            beatposition = listpos - len(window) + (window.index(max(window))) #Notate the position of the point on the X-axis
            #if (datapoint>150):
            RED_peaklist.append(beatposition) #Add detected peak to list
            window = [] #Clear marked ROI
            listpos += 1
            
    RED_peak = [dataset_RED[x] for x in RED_peaklist] 
    convertedRED = -dataset_RED;

    #Calculate moving average with 3s in both directions, then append do dataset
    mov_avg = pd.rolling_mean(convertedRED, window=int(hrw*fs)) #Calculate moving average

    #Impute where moving average function returns NaN, which is the beginning of the signal where x hrw
    avg_hr = (np.mean(convertedRED))
    mov_avg = [avg_hr if math.isnan(x) else x for x in mov_avg]
    mov_avg = [x*1.0004 for x in mov_avg] #For now we raise the average by 20% to prevent the secondary heart contraction from interfering, in part 2 we will do this dynamically
    hart_rollingmean = mov_avg #Append the moving average to the dataframe
    #Mark regions of interest    
        
    RED_minlist = []
    newvalleylist = []
    RED_min = []    
    window = []    
    listpos = 0    
    for datapoint in convertedRED:
        rollingmean = hart_rollingmean[listpos] #Get local mean
        if (datapoint < rollingmean) and (len(window) < 1): #If no detectable R-complex activity -> do nothing
            listpos += 1

        elif (datapoint > rollingmean): #If signal comes above local mean, mark ROI
            window.append(datapoint)
            listpos += 1
            
        else: #If signal drops below local mean -> determine highest point
            maximum = max(window)
            beatposition = listpos - len(window) + (window.index(max(window))) #Notate the position of the point on the X-axis
            #if (datapoint>150):
            RED_minlist.append(beatposition) #Add detected peak to list
            window = [] #Clear marked ROI
            listpos += 1

    RED_min = [-convertedRED[x] for x in RED_minlist] 
    num=len(RED_min)
    DC_RED=[]
    AC_RED=[]
    for i in range(1, num) :
        x=np.linspace(RED_minlist[i-1], RED_minlist[i])
        y=np.linspace(RED_min[i-1], RED_min[i])
        f=interp1d(x,y)
        DC_RED.append(f(RED_peaklist[i]))
      
    for i in range(1, num) :
        AC_RED.append(RED_peak[i]-DC_RED[i-1])

    RED_newpeaklist=RED_peaklist[pk_min:pk_max]
    
    #plt.figure(2)
    #plt.ylim(-500, 500)
    #plt.xlim(2000, 2100)
    #plt.title("Detected Peaks in IR and RED Signals for SPO2")
    #line_RED,= plt.plot(dataset_RED,label='RED')
    #plt.scatter(RED_peaklist, RED_peak, color='r')
    #plt.scatter(RED_minlist, RED_min, color='b')
    #plt.scatter(RED_newpeaklist, DC_RED,  color='g')
    #line_IR,=plt.plot(dataset_IR,label='IR')
    #plt.scatter(peaklist, IR_peak, color='y')
    #plt.scatter(minlist, IR_min, color='m')
    #plt.scatter(newpeaklist, DC_IR,  color='k')
    #plt.legend(handles=[line_RED, line_IR])
    #plt.savefig('figures/Figure09.png')
    #plt.draw()
    #plt.show
    spo2=[]

    for i in range(len(DC_IR)):
        r=(AC_RED[i]*DC_RED[i])/(DC_IR[i]*AC_IR[i])
        spo2.append(-45.060*r*r + 30.354 *r + 94.845)

    #spo2_peaktime = [time[x] for x in minlist]
    #print('SPO2 before = ',spo2)
    spo2 = spo2[4:]
    #spo2_peaktime = spo2_peaktime[4:]
    new_spo2 = [sp for sp in spo2 if sp > 94]
    #new_spo2_peaktime = [spo2_peaktime[i] for i, sp in enumerate(spo2) if sp > 94]
    #new_spo2 = new_spo2[1:]
    
    print('SPO2 (%) = ',new_spo2)
    #plt.figure(3)
    #plt.plot(new_spo2)
    #plt.title("Plot of SPO2")
    #plt.xlabel("Peaks")
    #plt.ylabel("SPO2 (%)")
    #plt.savefig(netid+'_figures/'+netid+'_'+activity_name+'_SPO2.png')
    #plt.draw()
    print("the mean of SPO2 for is {}%.\n".format(np.mean(new_spo2)))
    plt.show()
    
    
    return (new_spo2)
    

def find_ind(myList,myValue):
    '''
    This function finds the index of the first element in myList that is
    equal to or larger than myValue
    '''
    final_ind = -1
    for i,v in enumerate(myList):
        if v < myValue:
            final_ind = i
        else:
            break
    final_ind += 1

    return final_ind

    
def align_data(time, rate, peaktime):
    '''
    This function aligns the rate to the time steps according to the peak time
    '''
    peak_idx = []
    for pt in peaktime:
        peak_idx.append(find_ind(time,pt))
    aligned_rate = [None] * len(time)
    aligned_rate[:peak_idx[0]] = [rate[0]]*peak_idx[0]
    aligned_rate[peak_idx[-1]:] = [rate[-1]]*(len(aligned_rate)-peak_idx[-1])
    for i, rt in enumerate(rate):
        aligned_rate[peak_idx[i]:peak_idx[i+1]]=[rt]*(peak_idx[i+1]-peak_idx[i])
    
    return aligned_rate


def split_chunks(dataset, time_window=12, sliding_time=1, time_interval = 0.02):
    """
    Split original dataset into chunks for some time window and sliding time amount.

    Parameters
    ----------
    dataset : a 2D list: with len(dataset) = total time stamps, len(dataset[i]) = 21.
              dataset[i] = [time,IR1,RED1,X1,Y1,Z1,activity1,IR2,RED2,X2,Y2,Z2,activity2,IR3,RED3,X3,Y3,Z3,activity3,
                            IR4,RED4,X4,Y4,Z4,activity4,IR5,RED5,X5,Y5,Z5,activity5,IR6,RED6,X6,Y6,Z6,activity6]
    time_window : integer: the timespan during which one data chunk occurs, in unit of seconds.
    sliding_time : integer: the sliding time between two adjacent data chunks, in unit of seconds.
    time_interval : integer: the time interval between two adjacent time stamps, in unit of seconds.

    Returns
    -------
    data_chunks: a 3D list: with len(data_chunks) = (len(dataset)-n)/(n-m)+1,
                                 len(data_chunks[i]) = n, len(data_chunks[i][j]) = 21.
    
    Ex:
    test_chunks = split_chunks(test_data) : split the test dataset into chunks for a default
                                            time window of 12s and a sliding time of 1s.
    """
    n = int(time_window/time_interval) # group size
    m = int(n-sliding_time/time_interval) #int(n-100) #int(n-1) #0 #int(n/2) # overlap size
    data_chunks = [dataset[i:i+n] for i in range(0,len(dataset)-n+1, n-m)]
    
    return data_chunks


def find_average(feature_list):
    """
    Get the average of the feature from the three axes of the same activity in a time chunk.

    Parameters
    ----------
    feature_list : a 2D list of one feature, with len(feature_list) = number of activity types = 6,
                   len(feature_list[i]) = number of axes = 3.

    Returns
    -------
    avg_feature_list: a 1D list of averaged feature values for different activities, with len(avg_feature_list) = 6.
    
    Ex:
    avg_medium = find_average(medium) : find the average of the medium feature for each activity in a time chunk
    """
    avg_feature_list = [np.mean(np.array(feature_list[i])) for i in range(6)]
    
    return avg_feature_list


def extract_features_per_window(data_chunk, hasSingleActivity = False, isAverage = True):
    """
    Extract features by taking medium, (20,40,60,80)th percentile, maximum, and minimum from the same data column.

    Parameters
    ----------
    data_chunk : a 2D list of one time chunk of data: with len(data_chunks) = number of time stamps per chunk,
                                                           len(data_chunks[i]) = 21.
    hasSingleActivity : a boolean: to see if there are six activities or only one activity per chunk.
    isAverage : a boolean: to average over three axes of a feature of the same activity if true

    Returns
    -------
    medium, maximum, minimum : a 2D list of the medium/maximum/minimum feature for six activities of a chunk
                               if isAverage = False; or a 1D list if isAverage = True
    per20, per40, per60, per80 : a 2D list of the 20/40/60/80-th percentile feature for six activities of a chunk
                                 if isAverage = False; or a 1D list if isAverage = True
    
    Ex:
    medium, per20, per40, per60, per80, maximum, minimum = extract_features_per_window(test_chunk) : extract all
        seven features averaged over three axes for each activity of a test data chunk in seven 1D lists
    """
    data_chunk = np.asarray(data_chunk)
    #data_chunk = data_chunk-np.mean(data_chunk,axis=0)
    if not hasSingleActivity:
        # store features for excel columns [[3, 4, 5], [9, 10, 11], [15, 16, 17], [21, 22, 23], [27, 28, 29], [33, 34, 35]]
        medium = [[np.median(data_chunk[:,6*i+j]) for j in range(3,6)] for i in range(6)]
        per20 = [[np.percentile(data_chunk[:,6*i+j],20) for j in range(3,6)] for i in range(6)]
        per40 = [[np.percentile(data_chunk[:,6*i+j],40) for j in range(3,6)] for i in range(6)]
        per60 = [[np.percentile(data_chunk[:,6*i+j],60) for j in range(3,6)] for i in range(6)]
        per80 = [[np.percentile(data_chunk[:,6*i+j],80) for j in range(3,6)] for i in range(6)]
        maximum = [[np.amax(data_chunk[:,6*i+j]) for j in range(3,6)] for i in range(6)]
        minimum = [[np.amin(data_chunk[:,6*i+j]) for j in range(3,6)] for i in range(6)]
        if isAverage:
            avg_medium = find_average(medium); medium = avg_medium;
            avg_per20 = find_average(per20); per20 = avg_per20;
            avg_per40 = find_average(per40); per40 = avg_per40;
            avg_per60 = find_average(per60); per60 = avg_per60;
            avg_per80 = find_average(per80); per80 = avg_per80;
            avg_maximum = find_average(maximum); maximum = avg_maximum;
            avg_minimum = find_average(minimum); minimum = avg_minimum;
    else:
        # store features for columns [3,4,5]
        medium = [np.median(data_chunk[:,j]) for j in range(3,6)]
        per20 = [np.percentile(data_chunk[:,j],20) for j in range(3,6)]
        per40 = [np.percentile(data_chunk[:,j],40) for j in range(3,6)]
        per60 = [np.percentile(data_chunk[:,j],60) for j in range(3,6)]
        per80 = [np.percentile(data_chunk[:,j],80) for j in range(3,6)]
        maximum = [np.amax(data_chunk[:,j]) for j in range(3,6)]
        minimum = [np.amin(data_chunk[:,j]) for j in range(3,6)]
        if isAverage:
            avg_medium = np.mean(medium); medium = avg_medium;
            avg_per20 = np.mean(per20); per20 = avg_per20;
            avg_per40 = np.mean(per40); per40 = avg_per40;
            avg_per60 = np.mean(per60); per60 = avg_per60;
            avg_per80 = np.mean(per80); per80 = avg_per80;
            avg_maximum = np.mean(maximum); maximum = avg_maximum;
            avg_minimum = np.mean(minimum); minimum = avg_minimum;

    return (medium, per20, per40, per60, per80, maximum, minimum)


def extract_all_features(data_chunks, hasSingleActivity = False, isAverage=True, isReshaped=True):
    """
    Extract features for all the data chunks.

    Parameters
    ----------
    data_chunks : a 3D list of data chunks: with length of each dimension specified in split_chunks().
    hasSingleActivity : a boolean: to see if there are six activities or only one activity per chunk.
    isAverage : a boolean: to average over three axes of a feature of the same activity if true.
    isReshaped : a boolean: to flatten one feature of all data chunks from a 2D list to a 1D list.

    Returns
    -------
    all_medium, all_maximum, all_minimum, all_per20, all_per40, all_per60, all_per80 :
        a 3D list if isAverage = False and isReshaped = False;
        or a 2D list if isAverage = True and isReshaped = False;
        or a 2D list if isAverage = False and isReshaped = True;
        or a 1D list if isAveraged = True and isReshaped = True.
    
    Ex:
    all_medium, all_per20, all_per40, all_per60, all_per80, all_maximum, all_minimum
        = extract_all_features(test_chunks) : extract all seven features averaged over three axes
        for each activity of all test data chunks in seven 1D lists
    """
    all_medium = [None] * len(data_chunks)
    all_per20 = [None] * len(data_chunks)
    all_per40 = [None] * len(data_chunks)
    all_per60 = [None] * len(data_chunks)
    all_per80 = [None] * len(data_chunks)
    all_maximum = [None] * len(data_chunks)
    all_minimum = [None] * len(data_chunks)
    for i, dt_chunk in enumerate(data_chunks):
        all_medium[i], all_per20[i], all_per40[i], all_per60[i], all_per80[i], all_maximum[i], all_minimum[i] = extract_features_per_window(
            dt_chunk, hasSingleActivity = hasSingleActivity, isAverage=isAverage)
    if (not hasSingleActivity) and isReshaped:
        flat_medium = [item for sublist in all_medium for item in sublist]; all_medium = flat_medium;
        flat_per20 = [item for sublist in all_per20 for item in sublist]; all_per20 = flat_per20;
        flat_per40 = [item for sublist in all_per40 for item in sublist]; all_per40 = flat_per40;
        flat_per60 = [item for sublist in all_per60 for item in sublist]; all_per60 = flat_per60;
        flat_per80 = [item for sublist in all_per80 for item in sublist]; all_per80 = flat_per80;
        flat_maximum = [item for sublist in all_maximum for item in sublist]; all_maximum = flat_maximum;
        flat_minimum = [item for sublist in all_minimum for item in sublist]; all_minimum = flat_minimum;

    if not isAverage:
        tmp_medium = np.asarray(all_medium).T.tolist(); all_medium = tmp_medium;
        tmp_per20 = np.asarray(all_per20).T.tolist(); all_per20 = tmp_per20;
        tmp_per40 = np.asarray(all_per40).T.tolist(); all_per40 = tmp_per40;
        tmp_per60 = np.asarray(all_per60).T.tolist(); all_per60 = tmp_per60;
        tmp_per80 = np.asarray(all_per80).T.tolist(); all_per80 = tmp_per80;
        tmp_maximum = np.asarray(all_maximum).T.tolist(); all_maximum = tmp_maximum;
        tmp_minimum = np.asarray(all_minimum).T.tolist(); all_minimum = tmp_minimum;
    return (all_medium, all_per20, all_per40, all_per60, all_per80, all_maximum, all_minimum)


def extract_all_labels(data_chunks, hasSingleActivity=False, isReshaped=True, label=2):
    """
    Extract labels for all data chunks.

    Parameters
    ----------
    data_chunks : a 3D list of data chunks: with length of each dimension specified in split_chunks().
    hasSingleActivity : a boolean: to see if there are six activities or only one activity per chunk.
    isReshaped : a boolean: to flatten the labels of all data chunks from a 2D list to a 1D list
    label: an integer between 1 and 5: representing lying down (sleeping), sitting, walking, jogging, or running

    Returns
    -------
    labels : a 2D list of labels for six activities of all data chunks if isReshaped = False;
             or a 1D list for six activities if isReshaped = True;
             or a 1D list for single activities if hasSingleActivity=True.
    
    Ex:
    tr_labels = extract_all_labels(training_chunks) : extract all training labels for six activities 
        of all training data chunks in a 1D list
    """
    if not hasSingleActivity:
        if isReshaped:
            labels = [1,2,3,4,5,6] * len(data_chunks)
        else:
            labels = [[1,2,3,4,5,6]] * len(data_chunks)
    else:
        labels = [label] * len(data_chunks)

    return labels


def shuffle_data(X, Y=None):
    """
    Shuffle (randomly reorder) data in X and Y.

    Parameters
    ----------
    X : MxN numpy array: N feature values for each of M data points
    Y : Mx1 numpy array (optional): target values associated with each data point

    Returns
    -------
    X,Y  :  (tuple of) numpy arrays of shuffled features and targets
            only returns X (not a tuple) if Y is not present or None
    
    Ex:
    X2    = shuffleData(X)   : shuffles the rows of the data matrix X
    X2,Y2 = shuffleData(X,Y) : shuffles rows of X,Y, preserving correspondence
    """
    nx,dx = twod(X).shape
    Y = np.asarray(Y).flatten()
    ny = len(Y)

    pi = np.random.permutation(nx)
    X = X[pi,:]

    if ny > 0:
        assert ny == nx, 'shuffleData: X and Y must have the same length'
        Y = Y[pi] if Y.ndim <= 1 else Y[pi,:]
        return X,Y

    return X


def plot_test_result(netid, test_Y, test_Pred):
    """
    Plot test result using measured activity labels and predicted activity labels.

    Parameters
    ----------
    test_Y : a 1d list: all the measured activity labels from all the data chunks
    test_Pred : a 1d list: all the predicted activity labels for all the data chunks

    Returns
    -------
    None
    """
    plt.figure()
    plt.ylim(0.5, 5.5)
    plt.title("("+netid+") Activity Classification Test Result using SVM model\n (1->Sleeping, 2->Sitting, 3->Standing, 4->Walking, 5->Jogging, 6->Running)")
    line_Y, = plt.plot(test_Y,ls='-',label='measured activity')
    line_Pred, = plt.plot(test_Y,ls='-.',label='predicted_activity')
    plt.xlabel("Test Chunk")
    plt.ylabel("Activity")
    plt.legend(handles=[line_Y, line_Pred])
    plt.savefig(netid+'_figures/'+netid+'_test_result.png')
    #plt.show()
    return None

def plot_test_difference(netid, test_Y, test_Pred):
    """
    Plot test difference between predicted and measured activity labels.

    Parameters
    ----------
    test_Y : a 1d list: all the measured activity labels from all the data chunks
    test_Pred : a 1d list: all the predicted activity labels for all the data chunks

    Returns
    -------
    None
    """
    plt.figure()
    plt.ylim(-5, 5)
    plt.title("("+netid+") Activity Classification Test Difference Between\n Predicted and Measured Activity Labels using SVM model\n (1->Sleeping, 2->Sitting, 3->Standing, 4->Walking, 5->Jogging, 6->Running)")
    plt.plot(test_Y-test_Pred)
    plt.xlabel("Test Chunk")
    plt.ylabel("Activity Label Test Difference")
    plt.savefig(netid+'_figures/'+netid+'_test_difference.png')
    #plt.show()
    return None

def write_to_csv(mean_hr,mean_rr,mean_spo2,time,IR,RED,X,Y,Z,err_test,netid,activity_name):
    '''
    Write IR, RED, X, Y, Z, HR, RR, SPO2, Error Rate values to a new csv file for an activity
    '''
    IR = pd.Series(data=IR,name='IR')
    RED = pd.Series(data=RED,name='RED')
    AccX = pd.Series(data=X,name='X')
    AccY = pd.Series(data=Y,name='Y')
    AccZ = pd.Series(data=Z,name='Z')
    HR = pd.Series(data=[float(Decimal("%.3f" % mean_hr))]*len(time),name='Heart Rate (beats/min)')
    RR = pd.Series(data=[float(Decimal("%.3f" % mean_rr))]*len(time),name='Respiration Rate (breaths/min)')
    SPO2 = pd.Series(data=[float(Decimal("%.3f" % mean_spo2))]*len(time),name='SPO2 (%)')
    ErrRate = pd.Series(data=[float(Decimal("%.3f" % err_test))]*len(time),name='Error Rate (%)')
    col0 = IR.reset_index(drop=True)
    col1 = RED.reset_index(drop=True)
    col2 = AccX.reset_index(drop=True)
    col3 = AccY.reset_index(drop=True)
    col4 = AccZ.reset_index(drop=True)
    col5 = HR.reset_index(drop=True)
    col6 = RR.reset_index(drop=True)
    col7 = SPO2.reset_index(drop=True)
    col8 = ErrRate.reset_index(drop=True)
    All_to_Write = pd.concat([col0,col1,col2,col3,col4,col5,col6,col7,col8],axis=1)
    All_to_Write.to_csv(activity_name.title()+'/'+netid+'_assignment8_'+activity_name+'.csv', index = False, header = True)

    return None


if __name__ == '__main__':
    # obtain original data sheet
    netid = 'jiawec5'
    wb = xlrd.open_workbook(netid+'_team20_assignment8_input_data.xlsx')
    ws = wb.sheet_by_name('Sheet1')
    
    ### HR, RR, SPO2 Calculation
    # load data columns 
    time = [ws.cell_value(r, 0) for r in range(1,ws.nrows)]
    IR1 = [ws.cell_value(r, 1) for r in range(1,ws.nrows)] 
    RED1 = [ws.cell_value(r, 2) for r in range(1,ws.nrows)]
    X1 = [ws.cell_value(r, 3) for r in range(1,ws.nrows)]
    Y1 = [ws.cell_value(r, 4) for r in range(1,ws.nrows)]
    Z1 = [ws.cell_value(r, 5) for r in range(1,ws.nrows)]
    IR2 = [ws.cell_value(r, 7) for r in range(1,ws.nrows)]
    RED2 = [ws.cell_value(r, 8) for r in range(1,ws.nrows)]
    X2 = [ws.cell_value(r, 9) for r in range(1,ws.nrows)]
    Y2 = [ws.cell_value(r, 10) for r in range(1,ws.nrows)]
    Z2 = [ws.cell_value(r, 11) for r in range(1,ws.nrows)]
    IR3 = [ws.cell_value(r, 13) for r in range(1,ws.nrows)]
    RED3 = [ws.cell_value(r, 14) for r in range(1,ws.nrows)]
    X3 = [ws.cell_value(r, 15) for r in range(1,ws.nrows)]
    Y3 = [ws.cell_value(r, 16) for r in range(1,ws.nrows)]
    Z3 = [ws.cell_value(r, 17) for r in range(1,ws.nrows)]
    IR4 = [ws.cell_value(r, 19) for r in range(1,ws.nrows)]
    RED4 = [ws.cell_value(r, 20) for r in range(1,ws.nrows)]
    X4 = [ws.cell_value(r, 21) for r in range(1,ws.nrows)]
    Y4 = [ws.cell_value(r, 22) for r in range(1,ws.nrows)]
    Z4 = [ws.cell_value(r, 23) for r in range(1,ws.nrows)]
    IR5 = [ws.cell_value(r, 25) for r in range(1,ws.nrows)]
    RED5 = [ws.cell_value(r, 26) for r in range(1,ws.nrows)]
    X5 = [ws.cell_value(r, 27) for r in range(1,ws.nrows)]
    Y5 = [ws.cell_value(r, 28) for r in range(1,ws.nrows)]
    Z5 = [ws.cell_value(r, 29) for r in range(1,ws.nrows)]
    IR6 = [ws.cell_value(r, 31) for r in range(1,ws.nrows)]
    RED6 = [ws.cell_value(r, 32) for r in range(1,ws.nrows)]
    X6 = [ws.cell_value(r, 33) for r in range(1,ws.nrows)]
    Y6 = [ws.cell_value(r, 34) for r in range(1,ws.nrows)]
    Z6 = [ws.cell_value(r, 35) for r in range(1,ws.nrows)]
    
    ## 1-> Sleeping
    # calculate the heart rate and align to the original time steps
    #heart_rate_1, hr_peaktime_1 = calculate_HR(netid, 'sleeping', time, IR1, 0.9, 1.5, fs=50, order=5) #76.26
    #aligned_hr_1 = align_data(time, heart_rate_1, hr_peaktime_1)

    # calculate the respiration rate and align to the original time steps
    #respiration_rate_1, rr_peaktime_1 = calculate_RR(netid, 'sleeping', time, IR1, 0.250, 0.333, fs=50, order=5) #16.56
    #aligned_rr_1 = align_data(time, respiration_rate_1, rr_peaktime_1)
    
    # calculate the SPO2 and align to the original time steps
    #spo2_1, spo2_peaktime_1 = calculate_SPO2(netid, 'sleeping', time, IR1, RED1, 1.1, 2.0, 1.1, 2.2, fs=50, order=5) #98.11
    #aligned_spo2_1 = align_data(time, spo2_1, spo2_peaktime_1)

    ## 2-> Sitting
    # calculate the heart rate and align to the original time steps
    #heart_rate_2, hr_peaktime_2 = calculate_HR(netid, 'sitting', time, IR2, 0.8, 1.6, fs=50, order=5) #78.73
    #aligned_hr_2 = align_data(time, heart_rate_2, hr_peaktime_2)

    # calculate the respiration rate and align to the original time steps
    #respiration_rate_2, rr_peaktime_2 = calculate_RR(netid, 'sitting', time, IR2, 0.230, 0.333, fs=50, order=5) #16.52
    #aligned_rr_2 = align_data(time, respiration_rate_2, rr_peaktime_2)
    
    # calculate the SPO2 and align to the original time steps
    #spo2_2, spo2_peaktime_2 = calculate_SPO2(netid, 'sitting', time, IR2, RED2, 1.1, 2.1, 1.1, 2.1689, fs=50, order=5) #97.99
    #aligned_spo2_2 = align_data(time, spo2_2, spo2_peaktime_2)

    ## 3-> Standing
    # calculate the heart rate and align to the original time steps
    #heart_rate_3, hr_peaktime_3 = calculate_HR(netid, 'standing', time, IR3, 0.9, 1.7, fs=50, order=5) #78.63
    #aligned_hr_3 = align_data(time, heart_rate_3, hr_peaktime_3)

    # calculate the respiration rate and align to the original time steps
    #respiration_rate_3, rr_peaktime_3 = calculate_RR(netid, 'standing', time, IR3, 0.250, 0.333, fs=50, order=5) #16.53
    #aligned_rr_3 = align_data(time, respiration_rate_3, rr_peaktime_3)
    
    # calculate the SPO2 and align to the original time steps
    #spo2_3, spo2_peaktime_3 = calculate_SPO2(netid, 'standing', time, IR3, RED3, 1.1, 2.05, 1.1, 2.2, fs=50, order=5) #98.04
    #aligned_spo2_3 = align_data(time, spo2_3, spo2_peaktime_3)

    ## 4-> Walking
    # calculate the heart rate and align to the original time steps
    #heart_rate_4, hr_peaktime_4 = calculate_HR(netid, 'walking', time, IR4, 1.25, 1.7, fs=50, order=5) #91.35
    #aligned_hr_4 = align_data(time, heart_rate_4, hr_peaktime_4)

    # calculate the respiration rate and align to the original time steps
    #respiration_rate_4, rr_peaktime_4 = calculate_RR(netid, 'walking', time, IR4, 0.230, 0.350, fs=50, order=5) #17.06
    #aligned_rr_4 = align_data(time, respiration_rate_4, rr_peaktime_4)
    
    # calculate the SPO2 and align to the original time steps
    #spo2_4, spo2_peaktime_4 = calculate_SPO2(netid, 'walking', time, IR4, RED4, 1.1, 1.845, 1.1, 2.2, fs=50, order=5, pk_min = 0) #98.16
    #aligned_spo2_4 = align_data(time, spo2_4, spo2_peaktime_4)

    ## 5-> Jogging
    # calculate the heart rate and align to the original time steps
    #heart_rate_5, hr_peaktime_5 = calculate_HR(netid, 'jogging', time, IR5, 1.2, 1.85, fs=50, order=5) #95.64
    #aligned_hr_5 = align_data(time, heart_rate_5, hr_peaktime_5)

    # calculate the respiration rate and align to the original time steps
    #respiration_rate_5, rr_peaktime_5 = calculate_RR(netid, 'jogging', time, IR5, 0.245, 0.350, fs=50, order=5) #17.35
    #aligned_rr_5 = align_data(time, respiration_rate_5, rr_peaktime_5)

    # calculate the SPO2 and align to the original time steps
    #spo2_5, spo2_peaktime_5 = calculate_SPO2(netid, 'jogging', time, IR5, RED5, 0.8, 1.9, 0.8, 1.9, fs=50, order=5, pk_min = 0) #97.71
    #aligned_spo2_5 = align_data(time, spo2_5, spo2_peaktime_5)

    ## 6-> Running
    # calculate the heart rate and align to the original time steps
    #heart_rate_6, hr_peaktime_6 = calculate_HR(netid, 'running', time, IR6, 1.35, 2.11, fs=50, order=5) #109.08
    #aligned_hr_6 = align_data(time, heart_rate_6, hr_peaktime_6)

    # calculate the respiration rate and align to the original time steps
    #respiration_rate_6, rr_peaktime_6 = calculate_RR(netid, 'running', time, IR6, 0.234, 0.362, fs=50, order=5) #17.51
    #aligned_rr_6 = align_data(time, respiration_rate_6, rr_peaktime_6)
    
    # calculate the SPO2 and align to the original time steps
    #spo2_6, spo2_peaktime_6 = calculate_SPO2(netid, 'running', time, IR6, RED6, 1.0, 1.9885, 1.1, 2.2, fs=50, order=5, pk_min=0) #97.54
    #aligned_spo2_6 = align_data(time, spo2_6, spo2_peaktime_6)

    ### Activity Classification
    # obtain the training dataset and chunks from the first 80% dataset
    num_row = int(ws.nrows - 1)
    training_data = [[ws.cell_value(r, c) for c in range(ws.ncols)] for r in range(1,int(num_row*0.8+1))] 
    training_chunks = split_chunks(training_data, time_window=12, sliding_time=0.2)
    
    # obtain the test dataset and chunks from the rest 20% dataset
    test_data = [[ws.cell_value(r, c) for c in range(ws.ncols)] for r in range(int(num_row*0.8+1),ws.nrows)]
    test_chunks = split_chunks(test_data, time_window=12, sliding_time=0.2)

    # obtain features and labels for training
    #tr_medium, tr_per20, tr_per40, tr_per60, tr_per80, tr_maximum, tr_minimum = extract_all_features(
        #training_chunks, isAverage=False, isReshaped=True)
    #tr_features = [tr_medium, tr_per20, tr_per40, tr_per60, tr_per80, tr_maximum, tr_minimum]
    #all_tr_features = [tr_features[i][j] for i in range(7) for j in range(3)]; tr_features = all_tr_features;
    #tr_labels = extract_all_labels(training_chunks, isReshaped=True)

    # train the SVM model with the training dataset
    #train_X = np.asarray(tr_features).T
    #train_Y = np.asarray(tr_labels)
    #train_X, train_Y = shuffle_data(train_X, train_Y)
    #clf = SVC()
    #clf.fit(train_X, train_Y)

    # obtain features and labels for test
    #(te_medium, te_per20, te_per40, te_per60, te_per80, te_maximum, te_minimum) = extract_all_features(
        #test_chunks, isAverage=False, isReshaped=True)
    #te_features = [te_medium, te_per20, te_per40, te_per60, te_per80, te_maximum, te_minimum]
    #all_te_features = [te_features[i][j] for i in range(7) for j in range(3)]; te_features = all_te_features;
    #te_labels = extract_all_labels(test_chunks, isReshaped=True)

    # classify the test dataset using the trained model
    #test_X = np.asarray(te_features).T
    #test_Y = np.asarray(te_labels)
    #test_X, test_Y = shuffle_data(test_X, test_Y)
    #test_Pred = clf.predict(test_X)
    
    # report the test error rate
    #err_test = np.mean(test_Pred != test_Y)*100
    #print("The test error rate is {0:.3f}%.\n".format(err_test))

    # plot test difference between predicted and measured activity labels
    #plot_test_difference(netid, test_Y, test_Pred)

    ### Write IR, RED, X, Y, Z, HR, RR, SPO2, Error Rate values to a new csv file
    #write_to_csv(np.mean(heart_rate_1),np.mean(respiration_rate_1),np.mean(spo2_1),time,IR1,RED1,X1,Y1,Z1,err_test,netid,'sleeping')
    #write_to_csv(np.mean(heart_rate_2),np.mean(respiration_rate_2),np.mean(spo2_2),time,IR2,RED2,X2,Y2,Z2,err_test,netid,'sitting')
    #write_to_csv(np.mean(heart_rate_3),np.mean(respiration_rate_3),np.mean(spo2_3),time,IR3,RED3,X3,Y3,Z3,err_test,netid,'standing')
    #write_to_csv(np.mean(heart_rate_4),np.mean(respiration_rate_4),np.mean(spo2_4),time,IR4,RED4,X4,Y4,Z4,err_test,netid,'walking')
    #write_to_csv(np.mean(heart_rate_5),np.mean(respiration_rate_5),np.mean(spo2_5),time,IR5,RED5,X5,Y5,Z5,err_test,netid,'jogging')
    #write_to_csv(np.mean(heart_rate_6),np.mean(respiration_rate_6),np.mean(spo2_6),time,IR6,RED6,X6,Y6,Z6,err_test,netid,'running')
    
    ### show all the plots in the functions called earlier
    #plt.show()

