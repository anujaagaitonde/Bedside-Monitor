
#!/usr/bin/python

import threading
import multiprocessing as mp
import time

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
import numpy as np

import gui_copy as gui
import matplotlib.animation as animation

import ecg_lib as ecg

exitFlag = 0


def Tempread(Tempq,db,user):
      # Finds the correct device file that holds the temperature data
   base_dir = '/sys/bus/w1/devices/'
   device_folder = glob.glob(base_dir + '28*')[0]
   device_file = device_folder + '/w1_slave'
   #print ("Starting " + self.name)
   read_temp_init()
   #print("Temp Sensor Initialised")
   while True:
      temp = str(read_temp())
      #print(temp)
      db.child("/"+user['localId']+"/temperatureSensor/"+str(round(time.time()*1000))).set(str(temp))
      Tempq.put(temp)
      time.sleep(0.01)
      #print_time(self.name, 5, self.counter)

def PPGread (PPGirq,PPGredq,PPGirguiq):
      #print ("Starting " + self.name)
      m=max30102.MAX30102() #sensor initilisation
      #time.sleep(10)
      nread=100 #number of readings taken every second
      #plt.ion()
      ppgir=[]
      ppgred=[]
      print("PPG Sensor Initialised")
      while True:
          red, ir = m.read_sequential(nread)
          ppgir.extend(ir)
          ppgred.extend(red)
          #print("ir taken 1")
          #db.child("/"+user['localId']+"/ppgSensor/"+str(round(time.time()*1000))).set(ir)
         #print("ir pushed 1")
          PPGirq.put(ir)
          PPGirguiq.put(ir)
          PPGredq.put(red)
          #time.sleep(1)
          
def PPGprocess (PPGirq,PPGredq,hrq,rrq,spo2q,db,user):
   while True:
      ppgir=PPGirq.get()
      ppgred=PPGredq.get()
      db.child("/"+user['localId']+"/ppgSensor/"+str(round(time.time()*1000))).set(ppgir)
      hr=ppg.calculate_HR(ppgir,20.00,2.50,fs=100.0,order=1)
      rr=ppg.calculate_RR(ppgir,20.00,2.50,fs=100.0,order=1)
      #spo2=ppg.calculate_SPO2(ppgir,ppgred,20.00,2.5,20.00,2.5,fs=100,order=1)
      hrq.put(hr)
      rrq.put(rrq)
      #spo2q.put(spo2)
      time.sleep(1)

def ECGread(ecgrawq):
   print("reading ecG")
   e2=ecg.ECG()
   print("reading ecgG")
   while True:
      ecgarray=[]
      for i in range(300):
    # Read temperature (Celsius) from TMP102
    #temp_c = round(tmp102.read_temp(), 2)
    #for i in range(100):
         output = e2.analogInput(0)
         ecgarray.append(output)
         time.sleep(0.00333)
      #y_ecg.extend(e.read_store(300,600))
      #print("reading ecgG")
      ecgrawq.put(ecgarray)

def ECGprocess(ecgrawq,ecgfiltq,db,user):
   e=ecg.ECG()
   print("processing ECG")
   while True:
      ecgarray=ecgrawq.get()
      filtered_butter=e.realtime_butter(ecgarray,35,0,300,5)
      outputarray=filtered_butter.tolist()
      db.child("/"+user['localId']+"/ecgSensor/"+str(round(time.time()*1000))).set(outputarray)
      ecgfiltq.put(filtered_butter)
      time.sleep(1)

      
def GUIprocess(patient_name, dob_str, doctor_name,Tempq,PPGirq,PPGredq,hrq,rrq,spo2q,ecgrawq,ecgfiltq):
   print("GUI entered")
   g=gui.GUI("Omar Muttawa",'010100',"XXX YYY",Tempq,PPGirq,PPGredq,hrq,rrq,spo2q,ecgrawq,ecgfiltq)
   print("GUI Initilised")
   ani1 = animation.FuncAnimation(g.fig_ecg, g.animateecg, fargs = (g.y_ecg,), interval=20,blit=True) # animate graph every 20 ms
   ani2 = animation.FuncAnimation(g.fig_ppg, g.animateppg, fargs = (g.y_ppg,), interval=20,blit=True) # animate graph every 20 ms
   ani3 = animation.FuncAnimation(g.fig_resp, g.animaterr, fargs = (g.y_rr,), interval=20,blit=True)
   g.root.mainloop()

if __name__=='__main__':
   #Firebase configuration and sign in

   config = {
       "apiKey": "AIzaSyDFZ2WAZae-55_UK9KN_b9EbSAhhS-PTD8",
       "authDomain": "bedsidemonitor.firebaseapp.com",
       "databaseURL": "https://bedsidemonitor.firebaseio.com",
       "projectId": "bedsidemonitor",
       "storageBucket": "bedsidemonitor.appspot.com",
       "messagingSenderId": "680750955239",
       "appId": "1:680750955239:web:35f53ec6bc0227b6"
   }

   email="test@test.com"
   password="password"
   
   firebase = pyrebase.initialize_app(config)
   db = firebase.database()
   auth = firebase.auth()

   user = auth.sign_in_with_email_and_password(email, password)
   print("Connected to Firebase")

   pool=mp.Pool()
   manager=mp.Manager()
   
   Tempq=manager.Queue()
   PPGirq=manager.Queue()
   PPGredq=manager.Queue()
   PPGirguiq=manager.Queue()
   hrq=manager.Queue()
   rrq=manager.Queue()
   spo2q=manager.Queue()
   ecgrawq=manager.Queue()
   ecgfiltq=manager.Queue()


   #guiprocessp=pool.apply_async(GUIprocess, ("Omar Muttawa",'010100',"XXX YYY",Tempq,PPGirq,PPGredq,hrq,rrq,spo2q,ecgrawq,ecgfiltq))
   tempreadp=pool.apply_async(Tempread, (Tempq,db,user))
   ppgread=pool.apply_async(PPGread, (PPGirq,PPGredq,PPGirguiq))
   ppgprocessp=pool.apply_async(PPGprocess, (PPGirq,PPGredq,hrq,rrq,spo2q,db,user))
   ecgreadp=pool.apply_async(ECGread, (ecgrawq,))
   ecgprocess=pool.apply_async(ECGprocess, (ecgrawq,ecgfiltq,db,user))
   #guiprocessp=pool.apply_async(GUIprocess, ("Omar Muttawa",'010100',"XXX YYY",Tempq,PPGirq,PPGredq,hrq,rrq,spo2q,ecgrawq,ecgfiltq))   
   print("GUI entered")
   g=gui.GUI("Omar Muttawa",'010100',"XXX YYY",Tempq,PPGirguiq,PPGredq,hrq,rrq,spo2q,ecgfiltq)
   print("GUI Initilised")
   ani2 = animation.FuncAnimation(g.fig_ppg, g.animateppg, fargs = (g.y_ppg,), interval=1,blit=True) # animate graph every 20 ms
   ani3 = animation.FuncAnimation(g.fig_resp, g.animater, fargs = (g.y_rr,), interval=1,blit=True)
   ani1 = animation.FuncAnimation(g.fig_ecg, g.animateecg, fargs = (g.y_ecg,), interval=1,blit=True) # animate graph every 20 ms
   g.root.mainloop()
   pool.close()
   pool.join()
   print ("Exiting Main Thread")

