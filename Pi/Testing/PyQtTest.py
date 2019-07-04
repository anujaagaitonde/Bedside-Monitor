from pyqtgraph.Qt import QtGui, QtCore, QtWidgets
import numpy as np
import pyqtgraph as pg
import csv
import time
import sys
import random

class Plot2D():
    def __init__(self):
        self.traces = dict()
        #QtGui.QApplication.setGraphicsSystem('raster')
        self.app = QtGui.QApplication([])
        #mw = QtGui.QMainWindow()
        #mw.resize(800,800)
        self.win = pg.GraphicsWindow(title="LifeLine")
        self.win.resize(1000, 600)
        self.win.setWindowTitle("LifeLine")
        # Enable antialiasing for prettier plots
        pg.setConfigOptions(antialias=True)

        # header
        self.patient_name_canvas = self.win.addLabel(text="Patient: Omar Muttawa", row=0, col=0, rowspan=1, color='#FFFFFF')
        self.doctor_name_canvas = self.win.addLabel(text="Doctor: Mark Thompson", row=0, col=1, rowspan=1,
                                                     color='#FFFFFF')
        self.lifeline_tag_canvas = self.win.addLabel(text="© LifeLine 2019", row=0, col=6, rowspan=1,
                                                     color='#FFFFFF')

        # plots
        self.ecg_canvas = self.win.addPlot(title="ECG", row=1, col=0, rowspan=5, colspan=5)
        self.ecg_canvas.setLabel("bottom", "Time / seconds")
        self.ecg_canvas.hideAxis("left")

        self.ppg_canvas = self.win.addPlot(title="PPG", row=6, col=0, rowspan=5, colspan=5)
        self.ppg_canvas.setLabel("bottom", "Time / seconds")
        self.ppg_canvas.hideAxis("left")

        self.resp_canvas = self.win.addPlot(title="RESPIRATION", row=11, col=0, rowspan=5, colspan=5)
        self.resp_canvas.setLabel("bottom", "Time / seconds")
        self.resp_canvas.hideAxis("left")


        self.critical_button = QtWidgets.QPushButton('press me')
        # self.critical_canvas = self.win.addItem(self.critical_button)

        # digital values
        self.hr_title = self.win.addLabel(text="HEART RATE", row=1, col=6, rowspan=1, color='#61C535')
        self.hr_canvas = self.win.addLabel(text="--", row=2, col=6, rowspan=1, size='20pt', bold=True, color='#61C535')
        self.hr_label = self.win.addLabel(text="BPM", row=3, col=6, rowspan=1, color='#61C535')

        self.spo2_title = self.win.addLabel(text="SpO2", row=4, col=6, rowspan=1, color='#82DBE4')
        self.spo2_canvas = self.win.addLabel(text="--", row=5, col=6, rowspan=1, size='20pt', bold=True, color='#82DBE4')
        self.spo2_label = self.win.addLabel(text="%", row=6, col=6, rowspan=1, color='#82DBE4')

        self.temp_title = self.win.addLabel(text="TEMPERATURE", row=7, col=6, rowspan=1, color='#66D03C')
        self.temp_canvas = self.win.addLabel(text="--", row=8, col=6, rowspan=1, size='20pt', bold=True, color='#66D03C')
        self.temp_label = self.win.addLabel(text="˚C", row=9, col=6, rowspan=1, color='#66D03C')

        self.rr_title = self.win.addLabel(text="RESPIRATION RATE", row=10, col=6, rowspan=1, color='#F9F50C')
        self.rr_canvas = self.win.addLabel(text="--", row=11, col=6, rowspan=1, size='20pt', bold=True, color='#F9F50C')
        self.rr_units = self.win.addLabel(text="RPM", row=12, col=6, rowspan=1, color='#F9F50C')

        self.pr_title = self.win.addLabel(text="PULSE RATE", row=13, col=6, rowspan=1, color='#86E4F0')
        self.pr_canvas = self.win.addLabel(text="--", row=14, col=6, rowspan=1, size='20pt', bold=True, color='#86E4F0')
        self.pr_label = self.win.addLabel(text="BPM", row=15, col=6, rowspan=1, color='#86E4F0')

    def start(self):
        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
                    QtGui.QApplication.instance().exec_()

    def trace(self, name, dataset_x, dataset_y):
        if name in self.traces:
            self.traces[name].setData(dataset_x, dataset_y)
        else:
            if name == "ecg":
                self.traces[name] = self.ecg_canvas.plot(pen='#418934')
            elif name == "ecg_marker":
                self.traces[name] = self.ecg_canvas.plot(pen='#000000', style=QtCore.Qt.SolidLine)
            elif name == "ppg":
                self.traces[name] = self.ppg_canvas.plot(pen='#4AA1A4')
            elif name == "ppg_marker":
                self.traces[name] = self.ppg_canvas.plot(pen='#000000', style=QtCore.Qt.SolidLine)
            elif name == "max_ppg" or name == "min_ppg":
                self.traces[name] = self.ppg_canvas.plot(pen=pg.mkPen(color='#4AA1A4', style=QtCore.Qt.DotLine))
            elif name == "resp":
                self.traces[name] = self.resp_canvas.plot(pen='#418934')
            else:
                self.traces[name] = self.resp_canvas.plot(pen='#000000', style=QtCore.Qt.SolidLine)


## Start Qt event loop unless running in interactive mode or using pyside

if __name__ == '__main__':
    with open('ecg_data.csv', newline='') as csvfile:
        ecg_data = list(csv.reader(csvfile))
    ecg_data = np.squeeze(ecg_data)
    ecg_data = list(map(float, ecg_data))
    ecg_data = ecg_data - np.mean(ecg_data)

    with open('ppg_data.csv', newline='') as csvfile:
        ppg_data = list(csv.reader(csvfile))
    ppg_data = np.squeeze(ppg_data)
    ppg_data = list(map(float, ppg_data))
    ppg_data = ppg_data - np.mean(ppg_data)
    print(np.size(ppg_data))

    with open('resp_data.csv', newline='') as csvfile:
        resp_data = list(csv.reader(csvfile))
    resp_data = np.squeeze(resp_data)
    resp_data = list(map(float, resp_data))
    resp_data = resp_data - np.mean(resp_data)

    # append 10 seconds of zeros to beginning
    tmp = [0]*3000
    ecg_data = np.concatenate((tmp, ecg_data, ecg_data))

    tmp = [0]*1000
    ppg_data2 = np.concatenate((ppg_data[250:500], ppg_data[0:250]))
    ppg_data = np.concatenate((tmp, ppg_data, ppg_data, ppg_data2, ppg_data2, ppg_data, ppg_data2, ppg_data, ppg_data2, ppg_data, ppg_data2))

    tmp=[0]*1250
    resp_data = np.concatenate((tmp, resp_data, resp_data))

    p = Plot2D()
    i_ecg = 0
    j_ecg = 0
    ecg_x = np.arange(0, 10.0, 1/300)
    ecg_y = [0]*3000

    i_ppg = 0
    j_ppg = 0
    ppg_x = np.arange(0, 15.0, 1/100)
    ppg_y = [0]*1500
    extrema_ppg_x = np.arange(0, 15.0, 1/50)

    i_resp = 0
    j_resp = 0
    resp_x = np.arange(0, 10.0, 1/125)
    resp_y = [0]*1250
    resp_count = 1

    prev_start = 0

    def update():
        global p, i_ecg, j_ecg, ecg_x, ecg_y, ecg_data, i_ppg, j_ppg, ppg_x, ppg_y, ppg_data, i_resp, j_resp, resp_x, resp_y, resp_data, resp_count, prev_start
        start = time.time()
        print(start - prev_start)
        prev_start = start

        ecg_y[j_ecg:j_ecg + 15] = ecg_data[j_ecg + i_ecg*3000:j_ecg + i_ecg*3000 + 15]
        p.trace("ecg", ecg_x, ecg_y)
        #Tracing new value of ecg on to graph
        if j_ecg < 15 or j_ecg > 2985:
            pass
        else:
            ecg_marker_y = ecg_y[j_ecg - 15:j_ecg + 15]
            ecg_marker_x = np.arange((j_ecg - 15)/300, (j_ecg + 14.99)/300, 1/300)
            p.trace("ecg_marker", ecg_marker_x, ecg_marker_y)

        ppg_y[j_ppg:j_ppg + 5] = ppg_data[j_ppg + i_ppg*1500:j_ppg + i_ppg*1500 + 5]
        p.trace("ppg", ppg_x, ppg_y)
        #Tracing new value of ppg on to graph
        if j_ppg < 5 or j_ppg > 1495:
            pass
        else:
            ppg_marker_y = ppg_y[j_ppg - 5:j_ppg + 5]
            ppg_marker_x = np.arange((j_ppg - 5)/100, (j_ppg + 4.99)/100, 1/100)
            p.trace("ppg_marker", ppg_marker_x, ppg_marker_y)

        max_ppg = max(ppg_y)
        max_ppg = [max_ppg] * 750
        p.trace("max_ppg", extrema_ppg_x, max_ppg)
        min_ppg = min(ppg_y)
        min_ppg = [min_ppg] * 750
        p.trace("min_ppg", extrema_ppg_x, min_ppg)

        #Tracing new value of resp on to graph NOTE: MUST BE COMPLETED
        if (resp_count%4) == 0:
            resp_y[j_resp:j_resp + 7] = resp_data[j_resp + i_resp*1250:j_resp + i_resp*1250 + 7]
            p.trace("resp", resp_x, resp_y)
        else:
            resp_y[j_resp:j_resp + 6] = resp_data[j_resp + i_resp*1250:j_resp + i_resp*1250 + 6]
            p.trace("resp", resp_x, resp_y)

        if j_resp < 6 or j_resp > 1244:
            pass
        else:
            resp_marker_y = resp_y[j_resp - 6:j_resp + 6]
            resp_marker_x = np.arange((j_resp - 6)/125, (j_resp + 5.99)/125, 1/125)
            p.trace("resp_marker", resp_marker_x, resp_marker_y)

        j_ecg += 15
        j_ppg += 5
        if (resp_count%4) == 0:
            j_resp += 7
        else:
            j_resp += 6
        resp_count += 1

        #Relooping
        if j_ecg == 3000:
            j_ecg = 0
            if i_ecg == 5:
                i_ecg = 0
            else:
                i_ecg += 1

        if j_ppg == 1500:
            j_ppg = 0
            if i_ppg == 3:
                i_ppg = 0
            else:
                i_ppg += 1

        if j_resp == 1250:
            j_resp = 0
            if i_resp == 5:
                i_resp = 0
            else:
                i_resp += 1

        if (j_ecg%600) == 0:
            hr=random.randint(60,70)
            spo2=random.randint(90,100)
            temp=random.randint(36,38)
            rr=random.randint(15,20)
            pr=random.randint(60,70)
            p.hr_canvas.setText(str(hr))
            p.spo2_canvas.setText(str(spo2))
            p.temp_canvas.setText(str(temp))
            p.rr_canvas.setText(str(rr))
            p.pr_canvas.setText(str(pr))

    timer = QtCore.QTimer()
    timer.timeout.connect(update)
    timer.start(50)
    p.start()
