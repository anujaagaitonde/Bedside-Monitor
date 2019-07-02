#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Modules that need to be imported

from __future__ import absolute_import, division, print_function
import tensorflow as tf
import numpy as np
tf.logging.set_verbosity(tf.logging.INFO)
import os
import scipy.io
import random


# In[2]:


# GPU Online check (AWS EC2)

get_ipython().system('ln -sf /opt/bin/nvidia-smi /usr/bin/nvidia-smi')
get_ipython().system('pip install gputil')
get_ipython().system('pip install psutil')
get_ipython().system('pip install humanize')
import psutil
import humanize
import os
import GPUtil as GPU
GPUs = GPU.getGPUs()
# Colab only provides one GPU and it is not always guaranteed
gpu = GPUs[0]
def printm():
  process = psutil.Process(os.getpid())
  print("RAM Free: " + humanize.naturalsize( psutil.virtual_memory().available ), " | Proc size: " + humanize.naturalsize( process.memory_info().rss))
  print("GPU RAM Free: {0:.0f}MB | Used: {1:.0f}MB | Util {2:3.0f}% | Total {3:.0f}MB".format(gpu.memoryFree, gpu.memoryUsed, gpu.memoryUtil*100, gpu.memoryTotal))


# In[3]:


# Prints the amount of GPU RAM available
printm()


# In[19]:


data1 =np.reshape([2,3,4],(1,3,1))
print(data1)
max_len=3
data1 = data1[0:6]
print(data1.T)


# In[4]:


# A class to load the data from the files, process it and then prepare it for training and evaluation
# Import MIT-BIH arrhytmia dataset ( classses = 'A' = arrhytmia , 'N' = none, 'O'= other-arrhytmia, '~' = noise) 

class LoadECGData:

    def __init__(self, skip=0, omit=None, ref_file_path="training2017/REFERENCE.csv", data_folder_path="training2017/"): 
        self.skip = skip
        self.ref_file_path = ref_file_path
        self.data_folder_path = data_folder_path
        self.omit = omit
        self.ref = self.read_ref_file()
        

    # basic processing for the data-file    
    def process_data(self, data):
        fs = 300   # sampling rate of ECG signal from MIT website
        maxlen = 30 * fs   # 30 second intervals
        x = np.zeros((1, maxlen))
        data = np.nan_to_num(data)  # removing NaNs and Infs
        data = data[0, 0:maxlen]  # if more than 9000 samples, this line constrains it 
        data = data - np.mean(data)  # standardise the data
        data = data / np.std(data)
        x[0, :len(data)] = data.T  # padding sequence
        data = x
        return np.expand_dims(data, axis=2)  # required by Keras
    
    
    # a function for reading the headers of the files that need to examined
    # an omit clause is inserted in case you want to train without certain data( to balance imbalanced datasets)
    def read_ref_file(self):
        if self.omit:
          omit_label = self.omit + "\n"
        else:
          omit_label = ""
        ref = []
        print("\nReading reference text file (file path = '" + self.ref_file_path + "')...")
        ref_file = open(self.ref_file_path, "r")  # open the reference file with all the header names 
        for i in range(self.skip):
          line = ref_file.readline()
        line = ref_file.readline()
        while line:   # adding all the header names into an array for future purposes
            _, label = line.split(",")
            drop_prob = random.uniform (0,1)  # drop files from a particular class with a certain probability 
            if not label == omit_label or (label == omit_label and drop_prob < 0.75): # clause that inserts file names into an array
                ref.append(line.split(","))
            line = ref_file.readline()
        ref_file.close()
        print("\nReference file successfully read.")
        return ref
     
        
    # function to convert labels (training and evaluation) into one hot encoding for the loss function
    def make_label_onehot(self, label):
        if label == "A\n":
          return [1, 0, 0, 0]
        if label == "N\n":
          return [0, 1, 0, 0]
        if label == "O\n":
          return [0, 0, 1, 0]
        return [0, 0, 0, 1]
      
    def weight_samples(self,label):
        if label == "A\n":
          return 3.75
        if label == "N\n":
          return 1.25
        if label == "O\n":
          return 0.6
        return 0.6
    
    
    # function that reads the headers and inputs the data into training and evaluation arrays
    def read_data_files(self, batch_size, train_ratio=0.8):
        train_data = []
        train_labels = []
        eval_data = []
        eval_labels = []
        weight_array_train =[]
        weight_array_eval =[]
        num_train = round(len(self.ref) * train_ratio)  # the number of samples used for training (80% of what is fed in)
        print("\nLoading and processing data...")
        for i in range(num_train):
            file_name = self.data_folder_path + self.ref[i][0] + ".mat"  # getting a particular file name
            mat_data = scipy.io.loadmat(file_name)  # load the matrice
            data = mat_data['val']   # choose the required field
            processed_data = self.process_data(data)  # process data function called
            train_data.append(processed_data)
            train_labels.append(self.make_label_onehot(self.ref[i][1]))
            weight_array_train.append(self.weight_samples(self.ref[i][1]))
        for i in range(len(self.ref)-num_train):
            file_name = self.data_folder_path + self.ref[i + num_train][0] + ".mat"
            mat_data = scipy.io.loadmat(file_name)
            data = mat_data['val']
            processed_data = self.process_data(data)
            eval_data.append(processed_data)
            eval_labels.append(self.make_label_onehot(self.ref[i + num_train][1]))
            weight_array_eval.append(self.weight_samples(self.ref[i + num_train][1]))
        print("\nData loaded and processed (" + str(num_train) + " train, " + str(len(self.ref)-num_train) + " eval).")
        return np.array(train_data), np.array(train_labels), np.array(eval_data), np.array(eval_labels), np.array(weight_array_train), np.array(weight_array_eval)


# In[48]:


# function to define the structure of the ResNet ( in a tf.estimator format)

def get_res_block(input_layer, index, pool_toggle, k):
  
    # Variables
    conv_filters = 64
    conv_stride = 1
    kernel_size = 16
    pool_size = 2
    pool_stride = 2
    drop = 0.5
    
    if (index % 4 == 0) and (index > 0):  # increment k on every fourth residual block
        k += 1
        # increase depth by 1x1 Convolution case dimension shall change
        short = tf.layers.conv1d(
            inputs=input_layer,
            filters=conv_filters*k,
            kernel_size=1,
            activation=tf.nn.relu)
    else:
        short = input_layer

    batch_norm_1 = tf.layers.batch_normalization(inputs=short)  # first block for ResNet
    relu_1 = tf.nn.relu(features=batch_norm_1)
    dropout_1 = tf.layers.dropout(inputs=relu_1, rate=drop)
    conv_1 = tf.layers.conv1d(
        inputs=dropout_1,
        filters=conv_filters*k,
        kernel_size=kernel_size,
        strides=conv_stride,
        padding='same',
        kernel_initializer='he_normal',
        activation=tf.nn.relu)

    batch_norm_2 = tf.layers.batch_normalization(inputs=conv_1)  # second block for ResNet
    relu_2 = tf.nn.relu(features=batch_norm_2)
    dropout_2 = tf.layers.dropout(inputs=relu_2, rate=drop)
    conv_2 = tf.layers.conv1d(
        inputs=dropout_2,
        filters=conv_filters*k,
        kernel_size=kernel_size,
        strides=conv_stride,
        padding='same',
        kernel_initializer='he_normal')

    if pool_toggle:
        pool = tf.layers.max_pooling1d(inputs=conv_2, pool_size=pool_size, strides=pool_stride)
        # Right branch: shortcut connection
        pool_short = tf.layers.max_pooling1d(inputs=short, pool_size=pool_size, strides=pool_stride)
    else:
        pool = conv_2
        pool_short = short  # pool or identity

    return tf.concat([pool, pool_short], axis=1), k


def get_ecg_model(features, labels, mode):
    
    # Variables
    conv_filters = 64
    conv_stride = 1
    kernel_size = 16
    pool_size = 2
    pool_stride = 2
    drop = 0.5

    pool_toggle = True  # pool toggle every other residual block (end with 2^8)
    k = 1  # increment every 4th residual block

    # Input Layer
    input_layer = tf.reshape(features["x"], [-1, 9000, 1])  # input layer for model

    # Conv Block 1
    conv_1 = tf.layers.conv1d(
        inputs=input_layer,
        filters=conv_filters,
        kernel_size=kernel_size,
        strides=conv_stride,
        padding='same',
        kernel_initializer='he_normal')
    batch_norm_1 = tf.layers.batch_normalization(inputs=conv_1)
    relu_1 = tf.nn.relu(features=batch_norm_1)

    # Conv Block 2
    conv_2_1 = tf.layers.conv1d(
        inputs=relu_1,
        filters=conv_filters,
        kernel_size=kernel_size,
        strides=conv_stride,
        padding='same',
        kernel_initializer='he_normal')
    batch_norm_2 = tf.layers.batch_normalization(inputs=conv_2_1)
    relu_2 = tf.nn.relu(features=batch_norm_2)
    dropout_2 = tf.layers.dropout(inputs=relu_2, rate=drop)
   # second convolution layer in Block 2
    conv_2_2 = tf.layers.conv1d(
        inputs=dropout_2,
        filters=conv_filters,
        kernel_size=kernel_size,
        strides=conv_stride,
        padding='same',
        kernel_initializer='he_normal')
    pool_2 = tf.layers.max_pooling1d(inputs=conv_2_2, pool_size=pool_size, strides=pool_stride)

    # Block 2 Right Branch
    pool_2_right = tf.layers.max_pooling1d(inputs=relu_1, pool_size=pool_size, strides=pool_stride)

    # Block 2 Merge
    blocks = tf.concat([pool_2, pool_2_right], axis=1)

    for i in range(3):   # residual blocks. After testing, 3 residual blocks resulted in 'most' accurate output
        pool_toggle = not pool_toggle
        blocks, k = get_res_block(blocks, i, pool_toggle, k)

    # Final block
    batch_norm_18 = tf.layers.batch_normalization(inputs=blocks)
    relu_18 = tf.nn.relu(features=batch_norm_18)
    flatten = tf.layers.flatten(inputs=relu_18)
    logits = tf.layers.dense(inputs=flatten, units=4)
    
    # V1
    predictions = {
        "classes": tf.argmax(input=logits, axis=1),   # predict what class the ecg reading is [ 0 = 'A', 1 = 'N', 2 = 'O', 3='~']
        "probabilities": tf.nn.softmax(logits=logits, name="softmax_tensor")  # when model is served on azure, predict api ouputs this dictionary with results
    }
    
    if mode == tf.estimator.ModeKeys.PREDICT:    # tf estimator predict clause
        return tf.estimator.EstimatorSpec(mode=mode, predictions=predictions)  # return the prediction
    
    weights = features['weights']   # due to class imbalance, weighted samples used to give importance to certain classes
    loss = tf.losses.softmax_cross_entropy(onehot_labels=labels, logits=logits, weights = weights) # loss function
    
    if mode == tf.estimator.ModeKeys.TRAIN:  # tf estimator train clause
        optimizer = tf.train.MomentumOptimizer(learning_rate=0.00001, use_nesterov=True,momentum=0.9) # optimiser
        train_op = optimizer.minimize(
            loss=loss,
            global_step=tf.train.get_global_step())
        return tf.estimator.EstimatorSpec(mode=mode, loss=loss, train_op=train_op)
    
    label_tensor = tf.convert_to_tensor(labels)   # convert to tensor for functions below
    eval_metric_ops = {   # evaluation metrics 
        "accuracy": tf.metrics.accuracy(
            labels=tf.argmax(input=label_tensor, axis=1), predictions=tf.argmax(input=logits, axis=1)
        ) , 
        " auc_score": tf.metrics.auc(
            labels = label_tensor, predictions=predictions['probabilities']
        )
    }
    return tf.estimator.EstimatorSpec(
        mode=mode, loss=loss, eval_metric_ops=eval_metric_ops)

dataset_size = 8000
loader = LoadECGData()  # load the class 

# obtain the train and test dataset
train_data, train_labels, eval_data, eval_labels, weight_array_train, weight_array_eval = loader.read_data_files(dataset_size) # load the training and testing dataset

model_dir = "ecg_model"    # directory that the model is saved into
ecg_classifier = tf.estimator.Estimator(   # initialise the estimator
    model_fn=get_ecg_model, model_dir=model_dir)

# outputs tensors that you want to log for future
tensors_to_log = {"probabilities": "softmax_tensor"}
logging_hook = tf.train.LoggingTensorHook(
    tensors=tensors_to_log,every_n_iter=2)


# Training
train_input_fn = tf.estimator.inputs.numpy_input_fn(  # define the input function for train mode 
    x={"x": train_data, "weights" : weight_array_train},  # features 
    y=train_labels,
    batch_size=10,
    num_epochs=None,
    shuffle=True)

ecg_classifier.train(
    input_fn=train_input_fn,
    steps=600)   # number of run throughs

# converting the tf model into a pb format so that it can be used for inference from the cloud
serving_func = tf.estimator.export.build_raw_serving_input_receiver_fn({'x': tf.placeholder(tf.double, [None,9000,1])})   # serving function used to export saved_model
ecg_classifier.export_savedmodel('saved_mode_3', serving_func)

get_ipython().system('zip -r saved_model.zip saved_mode_3 ') # zip folder for downloading from Jupyter


# evaluation of model
batch_size =50  # cannot load all data for evaluation ( need to batch)
for i in range(1,int((len(eval_data)/batch_size)+1)):
    eval_input_fn = tf.estimator.inputs.numpy_input_fn(
        x={"x": eval_data[((batch_size*(i-1))):((batch_size*i)-1)], "weights" : weight_array_eval[((batch_size*(i-1))):((batch_size*i)-1)] }, # batching hardcoded as wanted to attempt it myself
        y=eval_labels[((batch_size*(i-1))):((batch_size*i)-1)],
        num_epochs=1,
        shuffle=False)

    eval_results = ecg_classifier.evaluate(input_fn=eval_input_fn)

# predict with the model and print results (in case a particular case is to be tested)


# items = <name of file on which inference needs to be done>
# mat_data = scipy.io.loadmat('training2017/'+items+'.mat')
# dat = mat_data['val']
# processed_data = loader.process_data(dat) 
# pred_input_fn = tf.estimator.inputs.numpy_input_fn(
#         x={"x": processed_data},
#         shuffle=False)
# pred_results = ecg_classifier.predict(input_fn=pred_input_fn)
# print(next(pred_results))

