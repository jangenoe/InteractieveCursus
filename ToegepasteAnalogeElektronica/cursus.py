import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from  matplotlib import patches
import scipy.signal as signal
#import pandas as pd  # nakijken of nog nodig
import numpy as np
from PySpice.Probe.Plot import plot
from PySpice.Spice.Parser import SpiceParser
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *
import schemdraw as schem
import schemdraw.elements as e
from ipywidgets import interact,FloatSlider
usewidgets=True;
    
def spicelisting(filename):
    with open(filename) as f:
        for line in f:
            print(line.strip())
    print()
    

def freqs_resp(ba_array,Dmin=1,Dmax=5,lowDB=-100, Npts = 1024,fsize=(6,4),legend=[],Printcoef=True,SaveGraf=False,grafname="c2.svg"):
    """
        b = ndarray of numerator coefficients
        a = ndarray of denominator coefficents
     Dmin = start frequency as 10**Dmin
     Dmax = stop frequency as 10**Dmax
    lowDB = lowest transfer function amplitude (in DB)
     Npts = number of points to plot; defult is 1024
    fsize = figure size; defult is (6,4) inches
    """
    f = np.logspace(Dmin,Dmax,Npts)
    fig, ax = plt.subplots(2,1 ,sharex=True,figsize=fsize)
    index=0
    for ba in ba_array:
        if Printcoef:
            ib=len(ba[0])-1
            print("Veelterm coefficienten teller: M=",ib)
            for bb in ba[0]:
                print ("b[",ib,"] =",bb)
                ib-=1
            ia=len(ba[1])-1
            print("Veelterm coefficienten noemer: N=", ia)
            for aa in ba[1]:
                print ("a[",ia,"] =",aa)
                ia-=1
        w,H = signal.freqs(ba[0],ba[1],2*np.pi*f)
        if legend==[]:
            ax[0].semilogx(f,20*np.log10(np.abs(H)))
        else:
            ax[0].semilogx(f,20*np.log10(np.abs(H)),label=legend[index])
            index+=1
        ax[1].semilogx(f,np.angle(H)/np.pi*180)
    ax[0].set_ylabel('Gain (dB)')
    ax[0].set_title('Frequency Response - Magnitude')
    ax[0].grid()
    ax[0].set_xlim([10**Dmin,10**Dmax]);
    ax[0].set_ylim([lowDB,5]);
    if not(legend==[]):
        ax[0].legend()
    ax[1].set_xlabel('Frequency (Hz)')
    ax[1].set_ylabel('Phase (graden)')
    ax[1].set_title('Frequency Response - Phase')
    ax[1].set_xlim([10**Dmin,10**Dmax]);
    ax[1].set_yticks([-180,-90,0,90,180])
    ax[1].grid();
    if SaveGraf:
        plt.savefig(grafname)
    plt.show();
def polen_nullen(z,p,circelarray,fsize=(6,6),Printcoef=True):
    if Printcoef:
        ib=1
        print("Lijst der nullen: M=", len(z))
        for bb in z:
            print ("z[",ib,"] =",bb)
            ib+=1
        ia=1
        print("Lijst der polen: N=", len(p))
        for aa in p:
            print ("p[",ia,"] =",aa)
            ia+=1
    fig, ax = plt.subplots(1,1, figsize=fsize)
    for circel in circelarray:
        ax.add_patch(patches.Ellipse((0,2*np.pi*circel[2]), width=4*np.pi*circel[0], height=4*np.pi*circel[1], fill=False, color='black', ls='dashed'))
    t1 = plt.plot(z.real, z.imag, 'go', ms=10)
    plt.setp( t1, markersize=5.0, markeredgewidth=1.5, markeredgecolor='k', markerfacecolor='g')
    t2 = plt.plot(p.real, p.imag, 'rx', ms=10)
    plt.setp( t2, markersize=5.0, markeredgewidth=1.5, markeredgecolor='r', markerfacecolor='r')
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    plt.show();