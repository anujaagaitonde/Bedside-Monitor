from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import matplotlib.animation as animation
import datetime as dt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Configure tkinter window
root = Tk()
root.configure(bg = "black")
root.geometry("800x480")

plt.style.use('dark_background')

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
        format_axis('p', ax)
        ax.plot(xar, yar, color="blue")
        graph_resp.draw()


xar = [] # Time array
y_ecg = [] # ECG data array
y_ppg = [] # PPG data array
y_resp = [] # Respiration data array
x=1

# ECG Graph pane
fig_ecg = Figure(figsize=(5,1), constrained_layout=True)
ax_ecg = fig_ecg.add_subplot(111)
format_axis('e', ax_ecg)
graph_ecg = FigureCanvasTkAgg(fig_ecg, master=root)
graph_ecg.get_tk_widget().grid(row=1, column=0)

# PPG Graph pane
fig_ppg = Figure(figsize=(5,1), constrained_layout=True)
ax_ppg = fig_ppg.add_subplot(111)
format_axis('p', ax_ppg)
graph_ppg = FigureCanvasTkAgg(fig_ppg, master=root)
graph_ppg.get_tk_widget().grid(row=2, column=0)

# Respiration Graph pane
fig_resp = Figure(figsize=(5,1), constrained_layout=True)
ax_resp = fig_resp.add_subplot(111)
format_axis('r', ax_resp)
graph_resp = FigureCanvasTkAgg(fig_resp, master=root)
graph_resp.get_tk_widget().grid(row=3, column=0)


# Update graph in real time
def animate(i, xar, y_ecg, y_ppg, y_resp):
    global x

    # Read data into arrays
    xar.append(dt.datetime.utcnow())
    y_ecg.append(x**2) 
    y_ppg.append(x)
    y_resp.append(x**3)

    # Limit arrays to store only the most recent 20 readings
    xar = xar[-20:]
    y_ecg = y_ecg[-20:]
    y_ppg = y_ppg[-20:]
    y_resp = y_resp[-20:]

    # remove - just for RT testing
    x += 1

    # Produce ECG plot
    plotter('e', ax_ecg, xar, y_ecg)

    # Produce PPG plot
    plotter('p', ax_ppg, xar, y_ppg)

    # Produce respiration plot
    plotter('r', ax_resp, xar, y_resp)

ani = animation.FuncAnimation(fig_ecg, animate, fargs = (xar, y_ecg, y_ppg, y_resp), interval=1000) # animate graph every 1000 ms

root.mainloop() # tkinter GUI window
