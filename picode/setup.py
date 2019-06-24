import subprocess

print("Installing libraries:")
subprocess.call(["sudo","apt-get","install","python3-pyrebase"])
print("Pyrebase installed")
subprocess.call(["sudo","apt-get","install","python3-datetime"])
print("Datetime installed")
subprocess.call(["sudo","apt-get","install","python3-matplotlib"])
print("Matplotlib installed")
subprocess.call(["sudo","apt-get","install","python3-numpy"])
print("Numpy installed")
subprocess.call(["sudo","apt-get","install","python3-tk"])
print("Tkinter installed")
print("ALL Libraries installed")

print("Configuring screen")
subprocess.call(["sudo","cp","config.txt", "/boot"])
print("Screen will rotate after reboot")

'''
print("Adding Main to boot")
subprocess.call(["sudo","cp", "lifelinemain.service","/lib/systemd/system/"])
subprocess.call(["sudo", "chmod", "644", "/lib/systemd/system/lifelinemain.service"])
subprocess.call(["sudo", "systemctl", "daemon-reload"])
subprocess.call(["sudo", "systemctl", "enable", "lifelinemain.service"])
print("Main.py added to boot please reboot!")
'''
