#!/usr/bin/python

import threading
import time
import numpy as np
#libraries for firebase
import pyrebase
import datetime

#libraries for TEMP Sensor
import os
import glob
from read_temp import read_temp_init,read_temp_raw,read_temp

#libraries required for PPG Sensor
import max30102_copy as max30102
import hrcalc
import matplotlib.pyplot as plt
import PPG_algorithms as ppg

#libraries required for ECG
import ecg_lib as ecg

#Import GUI
import gui_copy
import matplotlib.animation as animation


#Declaring Global Variables
exitFlag = 0

temparray=[27.5]
hrarray=[77]
spo2array=[97.5]
x_ecg=[]
y_ecg=[]
y_ppgir=[]
y_ppgred=[]
x_ppg=[]
ppgred=[]
y_resp=[]
x_resp=[]
resparray=[55]

class TempThread (threading.Thread):
   global temparray
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
   def run(self):
      global temparray
      print ("Starting " + self.name)
      read_temp_init()
      temp_high=False
      print("Temp Sensor Initialised")
      while True:
         temp=read_temp()
         if temp>28 and not temp_high:
            temp_high=True
            db.child("/"+user['localId']+"/critical/temperature/"+str(round(time.time()*1000))).set(True)
         if temp<=28:
            temp_high=False
         temparray.extend([round(temp,1)])
         db.child("/"+user['localId']+"/temperatureSensor/"+str(round(time.time()*1000))).set(str(temp))
         time.sleep(0.5)
      #print_time(self.name, 5, self.counter)
      print ("Exiting " + self.name)

class PPGThread (threading.Thread):
   global x_ppg,y_ppgir,y_ppgred,spo2array,hrarray,resparray
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
   def run(self):
      print ("Starting " + self.name)
      m=max30102.MAX30102() #sensor initilisation
      nread=100 #number of readings taken every second
      print("PPG Sensor Initialised")
      while True:
          #start=time.time()*1000
          for i in range(5):
             #start=time.time()*1000
             red, ir = m.read_sequential(nread)
             #y_ppgir.extend(ir)
             #y_ppgred.extend(red)
             #end=time.time()*1000
             #print(start)
             #x_ppg.extend(np.arange(start,end+1,round((end-start)/100)))
             #print("ir taken {}".format(i))
             time.sleep(0.10)
             db.child("/"+user['localId']+"/ppgSensor/"+str(round(time.time()*1000))).set(ir)
             #print("ir pushed {}".format(i))
          #hr_maxim, hrvalid, spo2, spo2valid = hrcalc.calc_hr_and_spo2(y_ppgir[-500:], y_ppgred[-500:])
          #hr=np.mean(ppg.calculate_HR(y_ppgir[-500:],20.00,2.50,fs=100.0,order=1))
          #spo2_stanford=ppg.calculate_SPO2(ppgir,ppgred,20.00,2.5,20.00,2.5,fs=100,order=1)
          #rr_stanford=ppg.calculate_RR(y_ppgir[-500:],20.00,2.50,fs=100,order=1)
          #print("calculated spo2 ")
          #if spo2 > 0:
             #db.child("/"+user['localId']+"/spo2Sensor/"+str(round(time.time()*1000))).set(spo2)
             #print("Pushed spo2 to Firebase")
          #print("SPO2_MAXIM: {}".format(spo2_maxim))
          #print("SPO2_STANFORD: {}".format(spo2_stanford))
          #print("HR_MAXIM: {}".format(hr_maxim))
          #print("HR_STANFORD: {}".format(hr))
          #sprint("RR_STANFORD: {}".format(rr_stanford))
          #spo2array.extend([round(spo2)])
          #hrarray.extend([round(hr)])
          #resparray.extend([round(np.mean(rr_stanford))])
      print ("Exiting " + self.name)

class ECGThread (threading.Thread):
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
   def run(self):
      e=ecg.ECG()
      global y_ecg,x_ecg
      print ("Starting " + self.name)
      while True:
         ecgarray=[]
         for i in range(900):
            output=e.analogInput(0)
            ecgarray.append(output)
            time.sleep(0.00333)
         filtered_butter=e.realtime_butter(ecgarray,35,0,300,5)
         outputarray=filtered_butter.tolist()
         #ecgraw=e.read_store(300,600)
         db.child("/"+user['localId']+"/ecgSensor/"+str(round(time.time()*1000))).set(outputarray)
         #y_ecg.extend(e.read_store(300,600))
         #print("ECG")
         time.sleep(0.5)
      #print_time(self.name, 5, self.counter)
      print ("Exiting " + self.name)

class GUIThread (threading.Thread):
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
   def run(self):
      print ("Starting " + self.name)
      g=gui_copy.GUI("Omar Muttawa",'010100',"XXX YYY")
      while True:
          print("GUIThread")
          print("GUI Initilised")
          ani = animation.FuncAnimation(g.fig_ecg, g.animate, fargs = (hrarray,spo2array,temparray,resparray,y_ecg,y_ppgir,y_resp), interval=500) # animate graph every 1000 ms
          g.root.mainloop()
      #print_time(self.name, 5, self.counter)
      print ("Exiting " + self.name)


#Firebase configuration and sign in

config = {
    apiKey: "AIzaSyDFZ2WAZae-55_UK9KN_b9EbSAhhS-PTD8",
    authDomain: "bedsidemonitor.firebaseapp.com",
    databaseURL: "https://bedsidemonitor.firebaseio.com",
    projectId: "bedsidemonitor",
    storageBucket: "bedsidemonitor.appspot.com",
    messagingSenderId: "680750955239",
    appId: "1:680750955239:web:35f53ec6bc0227b6"
}

email="test@test.com"
password="password"

firebase = pyrebase.initialize_app(config)
db = firebase.database()
auth = firebase.auth()

user = auth.sign_in_with_email_and_password(email, password)
print("Connected to Firebase")


# Create new threads
#thread4 = GUIThread(1, "GUIThread")
thread2 = PPGThread(2, "PPGThread")
thread3 = ECGThread(3, "ECGThread")
thread1 = TempThread(4, "TempThread")



# Start new Threads
thread1.start()
thread2.start()
thread3.start()
#thread4.start()

print ("Exiting Main Thread")
