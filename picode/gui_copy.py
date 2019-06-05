import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import matplotlib.animation as animation
import datetime as dt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class GUI():
    def __init__(self, patient_name, dob_str, doctor_name):
        self.root = tk.Tk()
        self.root.configure(bg = "black")
        self.root.geometry("800x480")
        plt.style.use('dark_background')
        self.patient_name=patient_name
        self.dob_str=dob_str
        self.doctor_name=doctor_name
        self.connected=True
        #Displaying Patient-Doctor info
        dob_obj = dt.datetime.strptime(self.dob_str, '%d%m%y')
        patient_info = tk.Label(self.root, text = "Name: "+self.patient_name+"  DOB: "+dt.datetime.strftime(dob_obj, '%d/%m/%y'), fg="white", bg="black")
        patient_info.grid(row=0, column=0, sticky='W')
        doctor_info = tk.Label(self.root, text = "Doctor: "+self.doctor_name, fg="white", bg="black")
        doctor_info.grid(row=0, column=1, sticky='W')
        #Heart Rate Digital Initilisation
        self.hr_info1 = tk.Label(self.root, text = "Heart Rate:", fg="green", bg="black", font=("Arial",14))
        self.hr_info2 = tk.Label(self.root, text = "--", fg="green", bg="black", font=("Arial", 40))
        self.hr_info3 = tk.Label(self.root, text = "bpm", fg="green", bg="black", font=("Arial", 14))
        self.hr_info1.grid(row=1, column=2)
        self.hr_info2.grid(row=2, column=2)
        self.hr_info3.grid(row=3, column=2)
        #SPO2 Digital Initilisaton
        self.spo2_info1 = tk.Label(self.root, text = "SpO2:", fg="yellow", bg="black", font=("Arial",14))
        self.spo2_info2 = tk.Label(self.root, text = "--", fg="yellow", bg="black", font=("Arial", 40))
        self.spo2_info3 = tk.Label(self.root, text = "%", fg="yellow", bg="black", font=("Arial", 14))
        self.spo2_info1.grid(row=4, column=2)
        self.spo2_info2.grid(row=5, column=2)
        self.spo2_info3.grid(row=6, column=2)
        #Temperature Digital Inilisation
        self.temp_info1 = tk.Label(self.root, text = "Temperature:", fg="red", bg="black", font=("Arial",14))
        self.temp_info2 = tk.Label(self.root, text = "--", fg="red", bg="black", font=("Arial", 40))
        self.temp_info3 = tk.Label(self.root, text = "˚C", fg="red", bg="black", font=("Arial", 14))
        self.temp_info1.grid(row=7, column=2)
        self.temp_info2.grid(row=8, column=2)
        self.temp_info3.grid(row=9, column=2)
        # Respiration Rate
        self.resp_info1 = tk.Label(self.root, text = "Respiration Rate:", fg="blue", bg="black", font=("Arial",14))
        self.resp_info2 = tk.Label(self.root, text = "--", fg="blue", bg="black", font=("Arial", 40))
        self.resp_info3 = tk.Label(self.root, text = "˚C", fg="blue", bg="black", font=("Arial", 14))
        self.resp_info1.grid(row=10, column=2)
        self.resp_info2.grid(row=11, column=2)
        self.resp_info3.grid(row=12, column=2)
        # ECG Graph pane
        self.fig_ecg = Figure(figsize=(6.7,1.3), constrained_layout=True)
        self.ax_ecg = self.fig_ecg.add_subplot(111)
        self.format_axis('e', self.ax_ecg)
        self.graph_ecg = FigureCanvasTkAgg(self.fig_ecg, master=self.root)
        self.graph_ecg.get_tk_widget().grid(row=1, column=0, columnspan=2, rowspan=4)
        # PPG Graph pane
        self.fig_ppg = Figure(figsize=(6.7,1.3), constrained_layout=True)
        self.ax_ppg = self.fig_ppg.add_subplot(111)
        self.format_axis('p', self.ax_ppg)
        self.graph_ppg = FigureCanvasTkAgg(self.fig_ppg, master=self.root)
        self.graph_ppg.get_tk_widget().grid(row=5, column=0, columnspan=2, rowspan=4)
        # Respiration Graph pane
        self.fig_resp = Figure(figsize=(6.7,1.3), constrained_layout=True)
        self.ax_resp = self.fig_resp.add_subplot(111)
        self.format_axis('r', self.ax_resp)
        self.graph_resp = FigureCanvasTkAgg(self.fig_resp, master=self.root)
        self.graph_resp.get_tk_widget().grid(row=9, column=0, columnspan=2, rowspan=4)
        # Report issue button
        self.report_button = tk.Button(self.root, text="REPORT ISSUE", command=self.report, width=70, height=2, fg="white", highlightbackground="black", bg="gray", activebackground="red")
        self.report_button.grid(row = 13, column=0, columnspan = 2, sticky='E')
    # Apply appropriate formatting to axes
    def format_axis(self,id, ax):
        if id == 'e':
            ax.set_ylabel('V', fontsize=8)
            ax.set_title("ECG",fontsize=9)
        elif id == 'p':
            ax.set_ylabel('PPG unit', fontsize=8)
            ax.set_title("PPG",fontsize=9)
        else:
            ax.set_ylabel('rpm', fontsize=8)
            ax.set_title("Respiration",fontsize=9)
        ax.set_xlabel("Time", fontsize=8)
        for tick in ax.get_xticklabels():
            tick.set_fontsize(6)
        for tick in ax.get_yticklabels():
            tick.set_fontsize(6)
    # Update graph
    def plotter(self,id, ax,yar):
        ax.cla()
        if id == 'e':
            self.format_axis('e', ax)
            ax.plot(yar, color="green")
            self.graph_ecg.draw()
        elif id == 'p':
            self.format_axis('p', ax)
            ax.plot(yar, color="yellow")
            self.graph_ppg.draw()
        else: 
            self.format_axis('r', ax)
            ax.plot(yar, color="blue")
            self.graph_resp.draw()
    # Set critical flag when report issue button is pressed - send this info to DB
    def report(self):
        critical = True
        critical_time = dt.datetime.utcnow()

    # Update graph in real time
    def animate(self,i,hr,spo2,temp,resp,y_ecg,y_ppgir,y_resp):
        print("animating")
        if self.connected:
           self.connection_status = tk.Label(self.root, text = "Connected", fg="green", bg="black")
           self.connection_status.grid(row=0, column=2)
        else:
           self.connection_status = tk.Label(self.root, text = "Disconnected", fg="red", bg="black")
           self.connection_status.grid(row=0, column=2)
        # Heart Rate
        self.hr_info2 = tk.Label(self.root, text = str(hr[-1]), fg="green", bg="black", font=("Arial", 40))
        #print("GUIheartrate: {}".format(hr[-1]))
        self.hr_info2.grid(row=2, column=2)
        # SpO2
        self.spo2_info2 = tk.Label(self.root, text = str(spo2[-1]), fg="yellow", bg="black", font=("Arial", 40))
        #print("GUIspo2: {}".format(spo2[-1]))
        self.spo2_info2.grid(row=5, column=2)
        # Temperature
        self.temp_info2 = tk.Label(self.root, text = str(temp[-1]), fg="red", bg="black", font=("Arial", 40))
        #print("GUItemp: {}".format(temp[-1]))
        self.temp_info2.grid(row=8, column=2)
        # Respiration Rate
        self.resp_info2 = tk.Label(self.root, text = str(resp[-1]), fg="blue", bg="black", font=("Arial", 40))
        #print("GUIrr: {}".format(resp[-1]))
        self.resp_info2.grid(row=11, column=2)
        # Produce ECG plot
        self.plotter('e', self.ax_ecg, y_ecg[-50:])
        # Produce PPG plot
        self.plotter('p', self.ax_ppg, y_ppgir[-17:])
        # Produce respiration plot
        self.plotter('r', self.ax_resp, y_resp[-20:])

#ani = animation.FuncAnimation(fig_ecg, animate, fargs = (), interval=1000) # animate graph every 1000 ms

#self.root.mainloop() # tkinter GUI window
