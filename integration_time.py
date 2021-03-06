#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 13:46:19 2021

@author: stefano.radice
"""

import numpy as np
import numpy.fft as ft
import matplotlib.pyplot as plt
#from cmath import sin, cos
from math import sin, cos,pi, atan2
import lock_in_amplifier as lock

amp = 2e-6;

phi = 1e-6;

f = 1e-5;

lun = 10;

npts = np.linspace(100,100000,lun)

tempo_campionamento = 1e-6;

t = [];

for i in range(lun):
    t.append(npts[i]*tempo_campionamento);
    

amp_ = [];
phi_ = [];

for i in range(lun):
    amp_i = [];
    phi_i = [];
    for j in range(10):
        l = lock.lock_in_amplifier(amp**2, amp, phi, int(npts[i]), tempo_campionamento, f);
        l.mixing();
        amp_j,phi_j = l.filtering(0, 0);
        amp_i.append(amp_j);
        phi_i.append(phi_j);
    amp_.append(np.std(amp_i));
    phi_.append(np.std(phi_i));
    print(i)

plt.figure();

plt.semilogy(t,amp_);
    