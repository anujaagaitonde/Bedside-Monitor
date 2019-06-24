import requests
import scipy.io
import json
import numpy as np
import csv
import matplotlib.pyplot as plt

# azure container instance from which the docker image is obtained

SERVER_URL = 'http://52.230.224.161:8501/v1/models/saved_model:predict'

# load data from lifeline (device) and then append to an array for inference
with open('ecg_data.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))
Lifeline_ecg_data=[]
for items in data:
        Lifeline_ecg_data.append(float(items[0]))

# same data processing function as one present in other python code file
def process_data(data):
        fs = 300
        maxlen = 30 * fs
        x = np.zeros((1, maxlen))
        data = np.nan_to_num(data)  # removing NaNs and Infs
        data = data[0, 0:maxlen]
        data = data - np.mean(data)
        data = data / np.std(data)
        x[0, :len(data)] = data.T  # padding sequence
        data = x
        return np.expand_dims(data, axis=2)

# for loop to conduct inference on two different matrix files
for index, items in enumerate(['training2017/A00067.mat','training2017/A00028.mat']):
        mat_data = scipy.io.loadmat(items) #load matrix file
        data1 = process_data(mat_data['val']) #process file
        data1 = data1.tolist()	 # convert to list for future processing
        data2 = json.dumps(data1[0])  # convert to json format 
        response = requests.post(SERVER_URL,data="{\"instances\":"+data2+"}") # conduct inference
        response_text = (response.text) # get the 'text' attribute of response
        print(response_text) # print the prediction and probability
        place  = response_text.find('classes') # printing the file name
        if index == 0:
            print(' The filenumber is A00067')
        else:
            print('The filenumbes is A00028')
        #print('For this particular segment, the ecg_recording is:' + response_text[place+10] )
        if response_text[place+10] == '0':  # if the prediction is '0' (a.k.a AF, then print corresponding statement)
            print('This patient has atrial fibrillation')
        else: # if the prediction is '1' (a.k.a N, then print corresponding statement)
            print('This person has a regular heartbeat')
        plt.plot(data1[0]) # plot the data
        plt.ylabel('ECG_level')
        plt.xlabel('Samples')
        plt.show()

Lifeline_ecg_data_1 = np.reshape(Lifeline_ecg_data,(1,9000,1)) # reshape the lifelife array to suit the model
processed_Lifeline_ecg_data = process_data(Lifeline_ecg_data) # same processing as above
processed_Lifeline_ecg_data = processed_Lifeline_ecg_data.tolist()  # convert to a list for future processing 
data4 = json.dumps(data3[0])
response = requests.post(SERVER_URL,data="{\"instances\":"+data4+"}") # conduct inference
response_text = (response.text)
print(response_text) # print prediction
place  = response_text.find('classes')
if response_text[place+10] == '1':
    print('Omar is all good')
else:
    print('Omar may have AF')
plt.plot(data3[0])  # plot the graph
plt.ylabel('ECG_level')
plt.xlabel('Samples')
plt.show()

