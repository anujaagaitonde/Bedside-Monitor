Lifeline – AF detection ML model

About

As part of the lifeline product, a model that could conduct real time Atrial fibrillation was deemed necessary. To conduct such a classification, two items were required: 
1.	Dataset 
2.	Model
Keeping this is mind, the first step was to find ECG datasets that classified AF from other heartbeat ECGs. Once this was obtained from the MIT website, the next step was to build a ML model for prediction. A shallow resnet model was determined to be the best fit. 

Installation

To run the model, clone: 

https://github.com/anujaagaitonde/Bedside-Monitor.git

Once cloned, go to the following folder:
	cd lifeline_ML 

Install the following libraries:
	pip install scipy 
	pip install requests
	pip install numpy
	pip install matplotlib

Run the script file:
	python3 script_final.py 

To conduct inference on the ML model, the shape of the input must be 1,9000,1 and the path in the script should be changed such that it points to the path where the data-file exists. 

Once the inference is complete, the prediction for that particular input is outputted. The following key is used:
0 = Atrial Fibrillation
1 = No atrial fibrillation
2 = Other arrhythmias
3 = Noisy data 

