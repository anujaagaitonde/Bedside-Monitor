
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import datetime as dt


fig = plt.figure()
fig, axs = plt.subplots(3)
xar = []
yar = []
x=1

def animate(i, xar, yar):
    global x

    # process data into arrays
    xar.append(dt.datetime.utcnow())
    yar.append(x**2) # read data

    # limit arrays to most recent 20 values
    xar = xar[-20:]
    yar = yar[-20:]

    x += 1

    # produce plots
    axs[0].clear()
    axs[0].plot(xar, yar)

    # axs[0].xticks(rotation='vertical')
    axs[0].set_title('ECG')
    axs[0].set(xlabel = 'Time', ylabel = '(V)')
    plt.sca(axs[0])
    plt.xticks(rotation = 45, ha = 'right')
    plt.tight_layout()

ani = animation.FuncAnimation(fig, animate, fargs = (xar, yar), interval=10)
plt.show()
