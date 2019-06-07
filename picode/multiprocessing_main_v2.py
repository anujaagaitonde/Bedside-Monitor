
#!/usr/bin/python

import threading
import multiprocessing as mp
import time
import sched

#libraries for firebase
import pyrebase
import datetime

#libraries for TEMP Sensor
import os
import glob
#from read_temp import read_temp_init,read_temp_raw,read_temp

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


def PPGTempread (PPGirq,PPGredq,PPGirguiq,Tempq,db,user):
      #print ("Starting " + self.name)
      m=max30102.MAX30102() #sensor initilisation
      #time.sleep(10)
      nread=100 #number of readings taken every second
      #plt.ion()
      ppgir=[]
      ppgred=[]
      print("PPG Sensor Initialised")

      #base_dir = '/sys/bus/w1/devices/'
      #device_folder = glob.glob(base_dir + '28*')[0]
      #device_file = device_folder + '/w1_slave'
      #print ("Starting " + self.name)
      #read_temp_init()
      #print("Temp Sensor Initialised")
      
      while True:
          red, ir = m.read_sequential(nread)
          ppgir.extend(ir)
          ppgred.extend(red)
          #print("ir taken 1")
          db.child("/"+user['localId']+"/ppgSensor/"+str(round(time.time()*1000))).set(ir)
          #print("ir pushed 1")
          PPGirq.put(ir)
          PPGirguiq.put(ir)
          PPGredq.put(red)
          #time.sleep(1)

          #temp = str(read_temp())
          #print(temp)
          #db.child("/"+user['localId']+"/temperatureSensor/"+str(round(time.time()*1000))).set(str(temp))
          Tempq.put(37.5)
          #print_time(self.name, 5, self.counter)
          
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

def ECGprocess(ecgfiltq, db, user):
   print("reading ecG")
   e=ecg.ECG()
   print("reading ecgG")
   while True:
      ecgarray=[]
      for i in range(300):
    # Read temperature (Celsius) from TMP102
    #temp_c = round(tmp102.read_temp(), 2)
    #for i in range(100):
         output = e.analogInput(0)
         ecgarray.append(output)
         time.sleep(0.00333)
      #y_ecg.extend(e.read_store(300,600))
      #print("reading ecgG")
      filtered_butter=e.realtime_butter(ecgarray,35,0,300,5)
      outputarray=filtered_butter.tolist()
      db.child("/"+user['localId']+"/ecgSensor/"+str(round(time.time()*1000))).set(outputarray)
      ecgfiltq.put(filtered_butter)
      #time.sleep(1)


      
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
       "apiKey": "AIzaSyB6mXwNEirNupF2wT28lclPJ9YjvFe1eQo",
       "authDomain": "mfmonitor-80a0d.firebaseapp.com",
       "databaseURL": "https://mfmonitor-80a0d.firebaseio.com",
       "projectId": "mfmonitor-80a0d",
       "storageBucket": "mfmonitor-80a0d.appspot.com",
       "messagingSenderId": "171419436747",
       "appId": "1:171419436747:web:e45ee688cbb5c5f0"
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
   ecgfiltq=manager.Queue()


   #guiprocessp=pool.apply_async(GUIprocess, ("Omar Muttawa",'010100',"XXX YYY",Tempq,PPGirq,PPGredq,hrq,rrq,spo2q,ecgrawq,ecgfiltq))
   ppgtempread=pool.apply_async(PPGTempread, (PPGirq,PPGredq,PPGirguiq,Tempq,db,user))
   ppgprocessp=pool.apply_async(PPGprocess, (PPGirq,PPGredq,hrq,rrq,spo2q,db,user))
   ecgprocess=pool.apply_async(ECGprocess, (ecgfiltq,db,user))
   #guiprocessp=pool.apply_async(GUIprocess, ("Omar Muttawa",'010100',"XXX YYY",Tempq,PPGirq,PPGredq,hrq,rrq,spo2q,ecgrawq,ecgfiltq))   
   print("GUI entered")
   g=gui.GUI("Omar Muttawa",'010100',"XXX YYY",Tempq,PPGirguiq,PPGredq,hrq,rrq,spo2q,ecgfiltq)
   print("GUI Initilised")
   ani2 = animation.FuncAnimation(g.fig_ppg, g.animateppg, fargs = (g.y_ppg,), interval=10,blit=True) # animate graph every 20 ms
   ani1 = animation.FuncAnimation(g.fig_ecg, g.animateecg, fargs = (g.y_ecg,), interval=10,blit=True) # animate graph every 20 ms
   ani3 = animation.FuncAnimation(g.fig_resp, g.animater, fargs = (g.y_rr,), interval=10,blit=True)
   #s = sched.scheduler(time.time, time.sleep)
   #s.enter(3000, 1, g.animatetemp, (s,))
   #s.run()
   g.root.mainloop()
   pool.close()
   pool.join()
   print ("Exiting Main Thread")

