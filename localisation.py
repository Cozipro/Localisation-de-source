# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 19:42:12 2021

@author: Corentin
"""
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.signal import correlate



Fs = 44100  #Sampling frequency
t = 1 #temps de record
N = Fs*t #Number of points

time = np.arange(N)/Fs

Devices = sd.query_devices()
print(Devices)

sd.default.device = 22 # set DEVICE_NUMBER

data = sd.rec(N, samplerate = Fs, blocking = True, channels = 2)



plt.figure()
plt.plot(time, data)
plt.show()

t_min = float(input("Temps de début du signal:   "))
t_max = float(input("Temps de fin du signal:  "))

x = data[int(t_min*Fs):int(t_max*Fs),0]
y = data[int(t_min*Fs):int(t_max*Fs),1]

Rxy = correlate(x,y)
l = np.arange(-len(x)+1,len(x))

delta_n = np.argmax(Rxy)
delta_t = abs(l[delta_n]/Fs)
d = 0.2
teta = np.arcsin(delta_t*344/d)

if l[delta_n] <0:
    print("Nord-ouest")
else:
    print("Nord-est")
print("Décalage de {} échantillons".format(l[delta_n]))

print("décalage de {} s".format(delta_t))
print("angle par rapport à la normale de l'antenne: {:.1f} rad".format(teta))
print("angle par rapport à la normale de l'antenne: {:.1f}°".format(teta*180/np.pi))


plt.figure()
plt.plot(l,Rxy)
plt.show()

print("Fini !")