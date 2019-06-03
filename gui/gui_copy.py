import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import matplotlib.animation as animation
import datetime as dt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class GUI():
    def __init__(self, patient_name, dob_str, doctor_name):
        root = tk.Tk()
        root.configure(bg = "black")
        root.geometry("800x480")
        plt.style.use('dark_background')
        self.patient_name=patient_name
        self.dob_str=dob_str
        self.doctor_name=doctor_name
        self.connected=True
        #Displaying Patient-Doctor info
        dob_obj = dt.datetime.strptime(self.dob_str, '%d%m%y')
        patient_info = tk.Label(root, text = "Name: "+self.patient_name+"  DOB: "+dt.datetime.strftime(dob_obj, '%d/%m/%y'), fg="white", bg="black")
        patient_info.grid(row=0, column=0, sticky='W')
        doctor_info = tk.Label(root, text = "Doctor: "+self.doctor_name, fg="white", bg="black")
        doctor_info.grid(row=0, column=1, sticky='W')
        #Heart Rate Digital Initilisation
        self.hr_info1 = tk.Label(root, text = "Heart Rate:", fg="green", bg="black", font=("Arial",14))
        self.hr_info2 = tk.Label(root, text = "--", fg="green", bg="black", font=("Arial", 40))
        self.hr_info3 = tk.Label(root, text = "bpm", fg="green", bg="black", font=("Arial", 14))
        self.hr_info1.grid(row=1, column=2)
        self.hr_info2.grid(row=2, column=2)
        self.hr_info3.grid(row=3, column=2)
        #SPO2 Digital Initilisaton
        self.spo2_info1 = tk.Label(root, text = "SpO2:", fg="yellow", bg="black", font=("Arial",14))
        self.spo2_info2 = tk.Label(root, text = "--", fg="yellow", bg="black", font=("Arial", 40))
        self.spo2_info3 = tk.Label(root, text = "%", fg="yellow", bg="black", font=("Arial", 14))
        self.spo2_info1.grid(row=4, column=2)
        self.spo2_info2.grid(row=5, column=2)
        self.spo2_info3.grid(row=6, column=2)
        #Temperature Digital Inilisation
        self.temp_info1 = tk.Label(root, text = "Temperature:", fg="red", bg="black", font=("Arial",14))
        self.temp_info2 = tk.Label(root, text = "--", fg="red", bg="black", font=("Arial", 40))
        self.temp_info3 = tk.Label(root, text = "˚C", fg="red", bg="black", font=("Arial", 14))
        self.temp_info1.grid(row=7, column=2)
        self.temp_info2.grid(row=8, column=2)
        self.temp_info3.grid(row=9, column=2)
        # Respiration Rate
        self.resp_info1 = tk.Label(root, text = "Respiration Rate:", fg="blue", bg="black", font=("Arial",14))
        self.resp_info2 = tk.Label(root, text = "--", fg="blue", bg="black", font=("Arial", 40))
        self.resp_info3 = tk.Label(root, text = "˚C", fg="blue", bg="black", font=("Arial", 14))
        self.resp_info1.grid(row=10, column=2)
        self.resp_info2.grid(row=11, column=2)
        self.resp_info3.grid(row=12, column=2)
        # ECG Graph pane
        self.fig_ecg = Figure(figsize=(6.7,1.3), constrained_layout=True)
        self.ax_ecg = self.fig_ecg.add_subplot(111)
        self.format_axis('e', self.ax_ecg)
        self.graph_ecg = FigureCanvasTkAgg(self.fig_ecg, master=root)
        self.graph_ecg.get_tk_widget().grid(row=1, column=0, columnspan=2, rowspan=4)
        # PPG Graph pane
        self.fig_ppg = Figure(figsize=(6.7,1.3), constrained_layout=True)
        self.ax_ppg = self.fig_ppg.add_subplot(111)
        self.format_axis('p', self.ax_ppg)
        self.graph_ppg = FigureCanvasTkAgg(self.fig_ppg, master=root)
        self.graph_ppg.get_tk_widget().grid(row=5, column=0, columnspan=2, rowspan=4)
        # Respiration Graph pane
        self.fig_resp = Figure(figsize=(6.7,1.3), constrained_layout=True)
        self.sax_resp = self.fig_resp.add_subplot(111)
        format_axis('r', self.ax_resp)
        self.graph_resp = FigureCanvasTkAgg(self.fig_resp, master=root)
        self.graph_resp.get_tk_widget().grid(row=9, column=0, columnspan=2, rowspan=4)
        # Report issue button
        self.report_button = tk.Button(root, text="REPORT ISSUE", command=report, width=70, height=2, fg="white", highlightbackground="black", bg="gray", activebackground="red")
        self.report_button.grid(row = 13, column=0, columnspan = 2, sticky='E')
    # Apply appropriate formatting to axes
    def format_axis(id, ax):
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
    def plotter(id, ax, xar, yar):
        ax.cla()
        if id == 'e':
            format_axis('e', ax)
            ax.plot(xar, yar, color="green")
            graph_ecg.draw()
        elif id == 'p':
            format_axis('p', ax)
            ax.plot(xar, yar, color="yellow")
            graph_ppg.draw()
        else: 
            format_axis('r', ax)
            ax.plot(xar, yar, color="blue")
            graph_resp.draw()
    # Set critical flag when report issue button is pressed - send this info to DB
    def report():
        critical = True
        critical_time = dt.datetime.utcnow()

    def display_digital(self,hr,spo2,temp,resp):
        # Connection status
        #connected = True
        if self.connected:
           self.connection_status = tk.Label(root, text = "Connected", fg="green", bg="black")
           self.connection_status.grid(row=0, column=2)
        else:
           self.connection_status = tk.Label(root, text = "Disconnected", fg="red", bg="black")
           self.connection_status.grid(row=0, column=2)
        # Heart Rate
        self.hr_info2 = tk.Label(root, text = str(hr), fg="green", bg="black", font=("Arial", 40))
        # SpO2
        self.spo2_info2 = tk.Label(root, text = str(spo2), fg="yellow", bg="black", font=("Arial", 40))
        # Temperature
        self.temp_info2 = tk.Label(root, text = str(temp), fg="red", bg="black", font=("Arial", 40))
        # Respiration Rate
        self.resp_info2 = tk.Label(root, text = str(resp), fg="blue", bg="black", font=("Arial", 40))
        
    # Update graph in real time
    def animate(self,i):
        global hr,spo2,temp
        global x_ecg,y_ecg,x_ppg,y_ppg,x_resp,y_resp
        display_digital(hr,spo2,temp,resp)
        # Produce ECG plot
        plotter('e', self.ax_ecg, x_ecg[-20:], y_ecg[-20:])
        # Produce PPG plot
        plotter('p', self.ax_ppg, x_ppg[-20:], y_ppgir[-20:])
        # Produce respiration plot
        plotter('r', self.ax_resp, x_resp[-20:], y_resp[-20:])

#ani = animation.FuncAnimation(fig_ecg, animate, fargs = (), interval=1000) # animate graph every 1000 ms

#root.mainloop() # tkinter GUI window
