
#!/usr/bin/python

import threading
import time

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
exitFlag = 0



class TempThread (threading.Thread):
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
   def run(self):
      print ("Starting " + self.name)
      read_temp_init()
      print("Temp Sensor Initialised")
      while True:
          temp = str(read_temp())
          print(temp)
          db.child("/"+user['localId']+"/temperatureSensor/"+str(round(time.time()*1000))).set(str(temp))
          time.sleep(0.5)
      #print_time(self.name, 5, self.counter)
      print ("Exiting " + self.name)

class PPGThread (threading.Thread):
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
   def run(self):
      print ("Starting " + self.name)
      m=max30102.MAX30102() #sensor initilisation
      #time.sleep(10)
      nread=2000 #number of readings taken every second
      #plt.ion()
      #x1=0
      #x2=100
      print("PPG Sensor Initialised")
      while True:
          ppgir=[]
          ppgred=[]
          red, ir = m.read_sequential(nread)
          ppgir.extend(ir)
          ppgred.extend(red)
          print(type(ir))
          print("ir taken 1")
          db.child("/"+user['localId']+"/ppgSensor/"+str(round(time.time()*1000))).set(ir)
          print("ir pushed 1")
          ppgir=np.asarray(ppgir)
          np.savetxt("ppgir_data.csv",ppgir,delimiter=",")
          ppgred=np.asarray(ppgred)
          np.savetxt("ppgred_data.csv",ppgred,delimiter=",")
          #hr, hrvalid, spo2, spo2valid = hrcalc.calc_hr_and_spo2(ppgir[:100], ppgred[:100])
          #spo2new=ppg.calculate_SPO2(ppgir,ppgred,20.00,2.5,20.00,2.5,fs=100,order=1)
          #rr=ppg.calculate_RR(ppgir,20.00,2.50,fs=100,order=1)
          hr=ppg.calculate_HR(ppgir,20.00,2.50,fs=100.0,order=1)
          #print("calculated spo2")
          #db.child("/"+user['localId']+"/spo2Sensor/"+str(round(time.time()*1000))).set(spo2)
          #print("Pushed spo2 to Firebase")
          #print("SPO2: {}".format(spo2new))
          #x1=x1+100
          #x2=x2+100
          #time.sleep(0.001)
      #print_time(self.name, 5, self.counter)
      print ("Exiting " + self.name)

class ECGThread (threading.Thread):
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
   def run(self):
      print ("Starting " + self.name)
      while True:
          print("ECGThread")
          time.sleep(1)      
      #print_time(self.name, 5, self.counter)
      print ("Exiting " + self.name)



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

 
# Finds the correct device file that holds the temperature data
#base_dir = '/sys/bus/w1/devices/'
#device_folder = glob.glob(base_dir + '28*')[0]
#device_file = device_folder + '/w1_slave'


# Create new threads
#thread1 = TempThread(1, "TempThread")
thread2 = PPGThread(2, "PPGThread")
thread3 = ECGThread(2, "ECGThread")

# Start new Threads
#thread1.start()
thread2.start()
thread3.start()

print ("Exiting Main Thread")
