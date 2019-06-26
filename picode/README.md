# Product Design History-Firmware

## Concept

### Initial Design Choices
3 ideas were pitched to the client ranging from a low price point ( £25 ) to a higher price point (£160). The main decisions revolved around which platform the monitor should be based around, dependent upon computing power requirements. The choices varied from :
* A cheap no-LCD Arduino-based solution
* Raspberry Pi Model 3b+ with LCD  
* The most expensive option was the Raspberry Pi Model 3b+ with LCD   with an Intel Compute Stick 2 to provide extra computing power.

The client selected the most expensive option and justified this decision by comparing the price of the monitor with that of existing patient monitoring systems costing upwards of £10,000. Moreover, the Intel Compute Stick is necessary to allow the use of offline machine learning algorithms to predict heart abnormalities, which was a critical feature to the client. 

### Sensor Choices 
The next decision made in the planning and construction phase was the  selection of sensors. The vital signs that the client wanted include ECG, PPG, temperature and respiration signals. Initially, inspiration for our sensor choices was drawn from a similar extension board made for the Raspberry Pi called the [Protocentral HealthyPi](http://healthypi.protocentral.com/) , and we aimed to benchmark the performance of this solution. The client brief indicated that we needed to exceed the performance of this device. The first sensor that we ordered was a Chinese clone of the sensor also used in Protocentral’s HealthyPi - included the ADS1292R ECG/Respiration sensor. The reason for this purchase was that this sensor calculated respiration signals through hardware as opposed to ECG-derived respiration signal that we settled with. This, in theory, should provide a more reliable signal than a software-derived respiration signal. Moreover, the ADS1292R was chosen given that no other dedicated respiration sensor was readily available. Whilst the ADS1292R solution would have been very convenient, it was incompatible with our Raspberry Pi, as it was initially designed for the Arduino. A custom Raspberry Pi library was written for the IC, however the sensor turned out to be temperamental and defective, so another sensor, the AD8232 was used. This ECG-only sensor meant that respiration signals had to be derived in software, however this sensor was approximately five times cheaper.

In regards to the PPG sensor, we initially tried to repurpose a commercial PPG sensor in a similar style to a [hobbyist device found on GitHub](https://github.com/BigCorvus/Physio?fbclid=IwAR3vFFrrheOALBNorfC2yaomDFmkHlitiyX7V35jlGn7bAjjqYdNBjYeiQg). This device used a [CMS50C](http://www.contecmed.com/index.php?page=shop.product_details&flypage=flypage.tpl&product_id=172&category_id=7&option=com_virtuemart&Itemid=592) pulse oximeter and tapped onto development points on the PCB to interface with an external microcontroller. However, the CMS50C pulse oximeter was no longer as it had been phased out in favour of the CMS50D device. Unfortunately, the CMS50D is unable to have it's signals tapped in the same fashion as the CMS50C. Moreover, our own implementation using the MAX30102 is more reproducible for the client in their later endeavours.

## Implementation and Build

### Modular Sensor Interface
Once all of the sensor choices were finalised, a Raspberry Pi hat was made. The PCB is designed to sit atop the Raspberry Pi and host the interface to the 3 sensors. Please see the Hardware folder for a detailed outline of all hardware implemented. of all the A key focus in the design of the device was the modularity, as it would allow the user to only plug in the sensors that are required for their specific application, driving down the costs. In pursuit of this goal, 3.5mm headphone jacks were placed on the PCB to allow the three different sensors to be detached as necessary. A 4-pole jack connector was used for all sensors. The PPG sensor initially required 5 wires however this requirement was trimmed down to 4 wires after some software tricks allowed the removal of an interrupt wire. 


### Modular Software Design
As the device is intended to be used modularly where the patient may only have one or two of the three available sensors plugged in to measure only some of their vital signs. All Software for the device had to be designed to allow for this functionality. To do so the multiprocessing library was split the software into processes for each sensor that run concurrently and make use of the raspberry pi's four cores. The following processes were defined:

**Tempprocess:** Responsible for reading temperature data from the DS18B20 sensor and pushing it to queues for displaying locally and pushing to the database. This is in a completely seperate process so that it is only run if the temperature sensor is plugged in and will not effect other processes if not plugged in.
**PPGread**: Responsible for reading PPG data from the MAX30102 sensor  and pushing into to queues for displaying locally, processing  and pushing to the database. This is in a completely seperate process so that it is only run if the MAX30102 sensor is plugged in. 
**PPGprocess:** Responsible for processing raw PPG data pushed from the PPGread queue and outputting spo2 and pulse rate values that are then pushed into queues for displaying locallyy and pushing to the database. This is in a completely seperate process from PPGread such that not to hinder the reading of the raw values from the MAX30102 with the intensive algorithms used to compute SPO2 and pulse rate. They will only run if data has been pushed to the PPG raw queues and hence  only if the MAX30102 sensor is plugged in.
**ECGprocess:** Responsible for reading ECG data from the MCP3008 ADC which in turn is reading from the analogue AD8232 sensor. The raw data is then filtered in real time and pushed to queues to be locally displayed and pushed to the database. This is in a completely seperate process so that it is only run if the ECG 3 lead electrode cable is plugged in.
**Respirationprocess:** Responsible for processing raw ECG data pushed from the  ECGraw

**DBprocess:**


### Scope for Improvement 
After the PCB was designed and manufactured in China, it was tested thoroughly. It was decided since the first meeting with the client that the device we make must have an LCD, not only does this allow the possibility for doctors to view the vital signs should they be physically close to the patient, it also gives the patient piece of mind that the device is working properly as they can view the signals. This is important as the ECG electrodes must be positioned properly to give useful signals and this allows the patient to evaluate the quality of the placement by the quality of the signals. However, due to the physical limitations of the headphone jack contacts, it was found that inserting some of the sensors whilst the Raspberry Pi was powered could lead to the sensor being damaged as improper insertion can cause short circuiting of the contacts. Future designs must ensure that this cannot happen, this may be mitigated by a 3.5mm switching jack socket.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5MDgwOTU1LDE0MTQ4NDQ0ODIsLTk2NT
cyOTUxNCwxMjU4MTMyMDA3LDMwMjA3ODksODA4MjY0NDU2LDE0
MTE1MTg0NzUsNzQ0ODEyMzM4XX0=
-->