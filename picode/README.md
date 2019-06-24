## Introduction
This folder contains all the firmware and software required in order to setup a lifeline monitor on a Raspberry Pi:

For setup and installation please see the [Getting-Started
](https://github.com/anujaagaitonde/Bedside-Monitor/wiki/Getting-Started) page of the Wiki:

## The following external public libraries are utilised:

### Firebase:
 - pyrebase

### PPG Processing:
 - numpy
 - scipy

### GUI:
- Matplotlib
- Tkinter

## The following libraries have been created:

### PPG Sensor and processing:
- max30102.py adapted from [Doug Burell's repo](https://github.com/doug-burrell/max30102/max30102.py)
- hrcalc.py adapted from [Doug Burrell's repo](https://github.com/doug-burrell/max30102/max30102.py)
- PPG_algorithms adapted from [Christine0313's repo
](https://github.com/Christine0313/CS244Fall2017) 

### ECG Sensor and processing:
- ECG_lib.py adapted from [PIA-Group's repo](https://github.com/PIA-Group/BioSPPy)
- ECG_processing.py

### Respiration processing:
- Resp_processing.py adapted from: [Raphaelvallat's gist](https://gist.github.com/raphaelvallat/55624e2eb93064ae57098dd96f259611)

# NOTE:
As detailed on the [
Getting Started](https://github.com/anujaagaitonde/Bedside-Monitor/wiki/Getting-Started)  page of the repo no libraries need to be manually installed, the setup script will install them automatically


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQxMTUxODQ3NSw3NDQ4MTIzMzhdfQ==
-->