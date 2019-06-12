
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
import max30102_doug as max30102
import hrcalc
import matplotlib.pyplot as plt
import PPG_algorithms as ppg
import numpy as np
#libraries required for animation
import gui_copy2 as gui
import matplotlib.animation as animation
#libraries required for ecg
import ecg_lib as ecgread
import ecg_processing as ecgprocess

exitFlag = 0

#libraries required for respiration
import resp_processing as resp


def PPGread (PPGirq,PPGredq,PPGirguiq,Tempq,db,user):
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
          PPGirq.put(ir)
          PPGirguiq.put(ir)
          PPGredq.put(red)
          Tempq.put(37)
          #db.child("/"+user['localId']+"/temperatureSensor/"+str(round(time.time()*1000))).set(str(37))
          #print_time(self.name, 5, self.counter)
'''          
def Tempprocess (Tempq,db,user):
      base_dir = '/sys/bus/w1/devices/'
      device_folder = glob.glob(base_dir + '28*')[0]
      device_file = device_folder + '/w1_slave'
      read_temp_init()
      print("Temp Sensor Initialised")
      while True:
          temp = str(round(read_temp(), 1))
          db.child("/"+user['localId']+"/temperatureSensor/"+str(round(time.time()*1000))).set(str(temp))
          Tempq.put(temp)
          time.sleep(1)
'''
      

def PPGprocess (PPGirq,PPGredq,prq,rrq,spo2q,db,user):
   ppgir = []
   ppgirpr = []
   ppgred = []
   while True:
      ppgirtmp = []
      qsizeir = PPGirq.qsize()
      for i in range(qsizeir):
          ppgirtmp.extend(PPGirq.get())
      ppgir.extend(ppgirtmp)
      ppgirpr.extend(ppgirtmp)
      qsizered = PPGredq.qsize()
      for i in range(qsizered):
          ppgred.extend(PPGredq.get())
      db.child("/"+user['localId']+"/ppgSensor/"+str(round(time.time()*1000))).set(ppgir)
      if len(ppgirpr) >= 1500:
         pr=ppg.calculate_HR(ppgirpr,20.00,2.50,fs=100.0)
         if pr > 30 and pr < 150:
            ppgirpr = ppgirpr[-1500:]
            prq.put(pr)
            db.child("/"+user['localId']+"/pulserate/"+str(round(time.time()*1000))).set(str(pr))
         else:
            prq.put(-1)
            db.child("/"+user['localId']+"/pulserate/"+str(round(time.time()*1000))).set("N/A")
            ppgirpr = []
      if len(ppgir) >= 500:
         _, _, spo2, spo2_valid=hrcalc.calc_hr_and_spo2(ppgir[-500:],ppgred[-500:])
         if spo2_valid:
            spo2 = round(spo2, 2)
            spo2q.put(int(spo2))
            db.child("/"+user['localId']+"/spo2/"+str(round(time.time()*1000))).set(str(spo2))
         else:
            spo2q.put(-1)
            db.child("/"+user['localId']+"/spo2/"+str(round(time.time()*1000))).set("N/A")
            ppgir = []
            ppgred = []
      time.sleep(1)

def ECGprocess(ecgrawq,ecgfiltq,db,user):
   print("reading ecG")
   e=ecgread.ECG()
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
      ecgarray=ecgprocess.volts(ecgarray)
      ecgrawq.put(ecgarray)
      ecg_filtered=e.realtime_butter(ecgarray,35,0,300,5)
      ecgfiltq.put(ecg_filtered)
      #db.child("/"+user['localId']+"/ecgSensor/"+str(round(time.time()*1000))).set(ecg_filtered)
      #time.sleep(1)

def Respirationprocess(ecgrawq,edrq,rrq,hrq,db,user):
   count = 0
   lastPeak = None
   edr_array = []
   sampling_rate=300
   resp_time=5
   rr_time=10
   ecgraw = []
   ecgrawtmp = []
   while True:
      qsize = ecgrawq.qsize()
      for i in range(qsize):
          ecgraw.extend(ecgrawq.get())
      if len(ecgraw) >= resp_time*sampling_rate:
            edr, hr, count, lastPeak = resp.get_respiration(ecgraw[-1500:],sampling_rate, count, lastPeak)
            edrq.put(edr)
            hrq.put(hr)
            #db.child("/"+user['localId']+"/edr/"+str(round(time.time()*1000))).set(edr)
            edr_array.extend(edr)
            ecgrawtmp.extend(ecgraw)
            ecgraw = []
            if len(ecgrawtmp) >= rr_time*sampling_rate:
                  rr=resp.get_rr(edr_array,10)
                  rr = int(rr)
                  rrq.put(rr)
                  #db.child("/"+user['localId']+"/rr/"+str(round(time.time()*1000))).set(rr)
                  edr_array=[]
                  ecgrawtmp=[]
                  
            
      
if __name__=='__main__':
   #Firebase configuration and sign in

   config = {
       "apiKey": "AIzaSyB3OD82TJeIDHOwiys2Cy_iD8wj5KxBvwU",
       "authDomain": "mfbedside.firebaseapp.com",
       "databaseURL": "https://mfbedside.firebaseio.com",
       "projectId": "mfbedside",
       "storageBucket": "mfbedside.appspot.com",
       "messagingSenderId": "477689150813",
       "appId": "1:477689150813:web:3e2c87dc310d4576"
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
   prq=manager.Queue()
   hrq=manager.Queue()
   rrq=manager.Queue()
   spo2q=manager.Queue()
   ecgfiltq=manager.Queue()
   ecgrawq=manager.Queue()
   edrq=manager.Queue()
   rrq=manager.Queue()

   ppgread=pool.apply_async(PPGread, (PPGirq,PPGredq,PPGirguiq,Tempq,db,user))
   ppgprocessp=pool.apply_async(PPGprocess, (PPGirq,PPGredq,prq,rrq,spo2q,db,user))
   ecgprocess=pool.apply_async(ECGprocess, (ecgrawq,ecgfiltq,db,user))
   respprocess=pool.apply_async(Respirationprocess, (ecgrawq,edrq,rrq,hrq,db,user))
   #tempprocess=pool.apply_async(Tempprocess, (Tempq,db,user))
   
   print("GUI entered")
   g=gui.GUI("Omar Muttawa",'140398',"Mark Thomas",Tempq,PPGirguiq,PPGredq,prq,hrq,edrq,rrq,spo2q,ecgfiltq,db,user)
   print("GUI Initilised")
   ani1 = animation.FuncAnimation(g.fig_ecg, g.animate, fargs = (g.y_ecg, g.y_ppg, g.y_rr,), interval=0,blit=True) # animate graph every 20 ms
   g.root.mainloop()
   pool.close()
   print ("Exiting Main Thread")

