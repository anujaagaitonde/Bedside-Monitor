import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import matplotlib.animation as animation
import datetime as dt
import time
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math
import sched
import queue

class GUI():
    def __init__(self, patient_name, dob_str, doctor_name,Tempq,PPGirq,PPGredq,prq,hrq,rrq,spo2q,ecgfiltq):
        self.root = tk.Tk()
        self.root.configure(bg = "black")
        self.root.geometry("800x480")
        self.root.attributes('-fullscreen', True)
        self.root.bind('<F11>', self.set_fullscreen)
        self.root.bind('<Escape>', self.exit_fullscreen)
        self.root.config(cursor='none')
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
        self.hr_info1 = tk.Label(self.root, text = "Heart Rate:", fg="green", bg="black", font=("Arial",10))
        self.hr_info2 = tk.Label(self.root, text = "--", fg="green", bg="black", font=("Arial", 25))
        self.hr_info3 = tk.Label(self.root, text = "bpm", fg="green", bg="black", font=("Arial", 10))
        self.hr_info1.grid(row=1, column=2)
        self.hr_info2.grid(row=2, column=2)
        self.hr_info3.grid(row=3, column=2)
        #SPO2 Digital Initilisaton
        self.spo2_info1 = tk.Label(self.root, text = "SpO2:", fg="yellow", bg="black", font=("Arial",10))
        self.spo2_info2 = tk.Label(self.root, text = "--", fg="yellow", bg="black", font=("Arial", 25))
        self.spo2_info3 = tk.Label(self.root, text = "%", fg="yellow", bg="black", font=("Arial", 10))
        self.spo2_info1.grid(row=4, column=2)
        self.spo2_info2.grid(row=5, column=2)
        self.spo2_info3.grid(row=6, column=2)
        #Temperature Digital Inilisation
        self.temp_info1 = tk.Label(self.root, text = "Temperature:", fg="red", bg="black", font=("Arial",10))
        self.temp_info2 = tk.Label(self.root, text = "--", fg="red", bg="black", font=("Arial", 25))
        self.temp_info3 = tk.Label(self.root, text = "˚C", fg="red", bg="black", font=("Arial", 10))
        self.temp_info1.grid(row=7, column=2)
        self.temp_info2.grid(row=8, column=2)
        self.temp_info3.grid(row=9, column=2)
        # Respiration Rate
        self.resp_info1 = tk.Label(self.root, text = "Respiration Rate:", fg="blue", bg="black", font=("Arial",10))
        self.resp_info2 = tk.Label(self.root, text = "--", fg="blue", bg="black", font=("Arial", 25))
        self.resp_info3 = tk.Label(self.root, text = "rpm", fg="blue", bg="black", font=("Arial", 10))
        self.resp_info1.grid(row=10, column=2)
        self.resp_info2.grid(row=11, column=2)
        self.resp_info3.grid(row=12, column=2)
        # Pulse
        self.pulse_info1 = tk.Label(self.root, text = "Pulse:", fg="purple", bg="black", font=("Arial",10))
        self.pulse_info2 = tk.Label(self.root, text = "--", fg="purple", bg="black", font=("Arial", 25))
        self.pulse_info3 = tk.Label(self.root, text = "bpm", fg="purple", bg="black", font=("Arial", 10))
        self.pulse_info1.grid(row=13, column=2)
        self.pulse_info2.grid(row=14, column=2)
        self.pulse_info3.grid(row=15, column=2)
        #Graphs Initilisation
        self.ecg_len=600
        self.ppg_len=200
        self.rr_len=200
        self.x_rr1=0
        self.x_ecg=list(range(0,self.ecg_len))
        self.x_ppg=list(range(0,self.ppg_len))
        self.x_rr=list(range(0,self.rr_len))
        #print(xs)
        self.y_ecg=[0]*self.ecg_len
        self.y_ppg=[0]*self.ppg_len
        self.y_rr=[0]*self.rr_len
        # ECG Graph pane
        self.fig_ecg = Figure(figsize=(6.7,1.3), tight_layout=True)
        self.ax_ecg = self.fig_ecg.add_subplot(111)
        self.format_axis('e', self.ax_ecg)
        self.graph_ecg = FigureCanvasTkAgg(self.fig_ecg, master=self.root)
        self.graph_ecg.get_tk_widget().grid(row=1, column=0, columnspan=2, rowspan=5)
        self.ecg_line, =self.ax_ecg.plot(self.x_ecg, self.y_ecg, color="#59eaed")
        self.ax_ecg.set_ylim([000,700])
        # PPG Graph pane
        self.fig_ppg = Figure(figsize=(6.7,1.3), tight_layout=True)
        self.ax_ppg = self.fig_ppg.add_subplot(111)
        self.format_axis('p', self.ax_ppg)
        self.graph_ppg = FigureCanvasTkAgg(self.fig_ppg, master=self.root)
        self.graph_ppg.get_tk_widget().grid(row=6, column=0, columnspan=2, rowspan=5)
        self.ppg_line, =self.ax_ppg.plot(self.x_ppg, self.y_ppg, color="#f51a18")
        self.ax_ppg.set_ylim([0,35000])
        # Respiration Graph pane
        self.fig_resp = Figure(figsize=(6.7,1.3), tight_layout=True)
        self.ax_resp = self.fig_resp.add_subplot(111)
        self.format_axis('r', self.ax_resp)
        self.graph = FigureCanvasTkAgg(self.fig_resp, master=self.root)
        self.graph.get_tk_widget().grid(row=11, column=0, columnspan=2, rowspan=5)
        self.rr_line, =self.ax_resp.plot(self.x_rr, self.y_rr, color="#3cd82c")
        self.ax_resp.set_ylim([-2,2])
        # Report issue button
        self.report_button = tk.Button(self.root, text="REPORT ISSUE", command=self.report, width=85, height=2, fg="white", bg="gray", activebackground="gray", activeforeground="white")
        self.report_button.grid(row = 16, column=0, columnspan = 3)
        #self.ecg_thread=ecgthread
        #self.ppg_thread=ppgthread
        #self.rr_thread=rrthread
        self.Tempq=Tempq
        self.PPGirq=PPGirq
        self.PPGredq=PPGredq
        self.prq=prq
        self.hrq=hrq
        self.rrq=rrq
        self.spo2q=spo2q
        self.ecgfiltq=ecgfiltq
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

    # Set critical flag when report issue button is pressed - send this info to DB
    def report(self):
        self.report_button.configure(bg="red", activebackground = "red")
        self.report_button.flash()
        critical = True
        critical_time = dt.datetime.utcnow()
        self.report_button.configure(bg="gray", activebackground = "gray")



    def updateDigital(self):
        try:
            spo2=self.spo2q.get_nowait()
            if spo2 == -1:
               self.spo2_info2.configure(text="N/A")
            else:
               self.spo2_info2.configure(text=str(spo2))
        except:
            pass
        try:
            pr=self.prq.get_nowait()
            if pr == -1:
                self.pulse_info2.configure(text="N/A")
            else:
                self.pulse_info2.configure(text=str(pr))
        except:
            pass
        try:
            hr=self.prq.get_nowait()
            if hr == -1:
                self.hr_info2.configure(text="N/A")
            else:
                self.hr_info2.configure(text=str(hr))
        except:
            pass
        try:
            temp=self.Tempq.get_nowait()
            self.temp_info2.configure(text=str(temp))
        except:
            pass
        try:
            rr=self.rrq.get_nowait()
            self.resp_info2.configure(text=str(rr))
        except:
            pass
        
    def set_fullscreen(self, event=None):
        self.root.attributes('-fullscreen', True)
        return "break"

    def exit_fullscreen(self, event=None):
        self.root.attributes('-fullscreen', False)
        return "break"

    def animate(self, i, y_ecg, y_ppg, y_resp):
            
        global x_ecg
        y_ecg.extend(self.ecgfiltq.get()) 
        y_ecg = y_ecg[-self.ecg_len:]
        self.ecg_line.set_ydata(y_ecg)

        global x_ppg
        qsize = self.PPGirq.qsize()
        for i in range(qsize):
            y_ppg.extend(self.PPGirq.get()) 
        y_ppg = y_ppg[-self.ppg_len:]
        self.ppg_line.set_ydata(y_ppg)
        

        global x_resp
        y_resp.append(math.sin(self.x_rr1/2*math.pi)) 
        y_resp = y_resp[-self.rr_len:]
        self.x_rr1 += 1
        if (self.x_rr1/(2*math.pi))==1:
            self.x_rr1=0
        self.rr_line.set_ydata(y_resp)
        self.updateDigital()

        return self.ecg_line, self.ppg_line, self.rr_line,
        
        
#ani = animation.FuncAnimation(fig_ecg, animate, fargs = (), interval=1000) # animate graph every 1000 ms

#self.root.mainloop() # tkinter GUI window
