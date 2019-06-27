#
# Lifeline – AF detection ML model

**About**

As part of the lifeline product, a model that could conduct real time Atrial fibrillation was deemed necessary. To conduct such a classification, two items were required:

1. Dataset
2. Model

Keeping this is mind, the first step was to find ECG datasets that classified AF from other heartbeat ECGs. Once this was obtained from the MIT website, the next step was to build a ML model for prediction. A shallow resnet model was determined to be the best fit.

**Installation**

1. To run the model, clone:

``` https://github.com/anujaagaitonde/Bedside-Monitor.git ```

2. Once cloned, go to the following folder:

``` cd lifeline\_ML ```

3. Install the following libraries:

* pip install scipy

* pip install requests

* pip install numpy

* pip install matplotlib

4. Run the script file:

 ```python3 script\_final.py ```

5. To conduct inference on the ML model, the shape of the input must be 1,9000,1 and the path in the script should be changed such that it points to the path where the data-file exists.

Once the inference is complete, the prediction for that particular input is outputted:
<img width="1267" alt="image" src="https://user-images.githubusercontent.com/37315285/60135517-cd336a00-9799-11e9-9bff-17ff17b8a2cf.png">



