import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from  matplotlib import patches
import scipy.signal as signal
import numpy as np
from PySpice.Probe.Plot import plot
from PySpice.Spice.Parser import SpiceParser
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *
import schemdraw
from schemdraw.elements import *
import skrf as rf
from ipywidgets import interact,FloatSlider

from IPython import display
import os

def spicelisting(filename,firstline=0,lastline=10000):
    ff=""
    with open(filename) as f:
        for i,line in enumerate(f):
            if i>=firstline and i<lastline:
                ff+=line.strip()+"\r"
    return display.Code(data=ff, language='spice')

if 'USEWIDGETS' in os.environ:
    usewidgets= (os.getenv('USEWIDGETS')=='True')
else:
    usewidgets=False;
    
human_format = lambda num: [f'{num/10**(3*(i-8)):.2f}{k}' for i, k in enumerate('yzafpnµm kMGTPEZY')  if num >= 10**(3*(i-8)) * 0.9995][-1]

def Sallen_and_Key_LP_draw(labels=True, Freq=1e6,angle=60,Cref=16e-12,Rout=1e5,inches_per_unit=0.5, Resistorlength=2,
                           voutlabel='$V_{out}$',vinlabel='$V_{in}$'):
    if labels:
        Rlabel='R'
        Clabel='C'
        R1label='R1'
        R2label='R2'
    else:
        k=2-2*np.cos(angle/180*np.pi)
        Rlabel=human_format(1/Cref/2/np.pi/Freq)+'$\Omega$'
        Clabel=human_format(Cref)+'F'
        R1label=human_format(Rout/(1+k))+'$\Omega$'
        R2label=human_format(k*Rout/(1+k))+'$\Omega$'
    with schemdraw.Drawing(inches_per_unit=inches_per_unit) as d:
     d += (op := Opamp(flip=True))
     d += ( Line( d='left', l=1.75, xy=op.in2))
     d += (R2 := Resistor( d='left',l=Resistorlength, label=Rlabel))
     d += (R1 := Resistor( d='left',l=Resistorlength, label=Rlabel))
     d += ( Dot(open=True, label=vinlabel))
     d += ( Dot( xy=R2.start))
     d += ( Capacitor( d='down', l=Resistorlength, label=Clabel))
     d += ( Ground())
     d += ( Dot( xy=R2.end))
     d += ( Line( d='up', l=1.5))
     d += ( Capacitor( d='right', tox=op.out+1, label=Clabel))
     d += ( Line( d='down', toy=op.out))
     d += ( Dot())
     d += ( Line( d='left', l=0.5, xy=op.in1))
     d += ( Line( d='down', l=1.25))
     d += (vm := Dot())
     d += ( Resistor( d='down', l=Resistorlength, label=R1label))
     d += ( Ground())
     d += ( Resistor( xy=vm.start, d='right', label=R2label, tox=op.out+0.5))
     d += ( Line( d='up', toy=op.out))
     d += ( Dot())
     d += ( Line( d='right', xy=op.out, l=2))
     d += ( Dot(open=True, label=voutlabel))
    return
    
def first_Order_LP_draw(labels=True, Freq=1e6,Cref=16e-12,inches_per_unit=0.5, Resistorlength=2, LFgain=1,
                           voutlabel='$V_{out}$',vinlabel='$V_{in}$'):
    if labels:
        Clabel='$C_2$'
        R1label='$R_1$'
        R2label='$R_2$'
    else:
        R2=1/Cref/2/np.pi/Freq
        R2label=human_format(R2)+'$\Omega$'
        Clabel=human_format(Cref)+'F'
        R1label=human_format(R2/LFgain)+'$\Omega$'
    with schemdraw.Drawing(inches_per_unit=inches_per_unit) as d:
     d += (op := Opamp())
     d += ( Line( d='left', xy=op.in2, l=d.unit/4))
     d += ( Line( d='down', l=d.unit/5))
     d += ( Ground())
     d += ( Line( d='left', xy=op.in1, l=d.unit/6))
     d += (nn1 := Dot())
     d += (Rin := Resistor( d='left',  botlabel=R1label))
     d += ( Line( d='left', l=d.unit/6))
     d += ( Dot(open=True,lftlabel=vinlabel))
     d += ( Line( d='up',xy=nn1.start, l=d.unit/2))
     d += ( Dot())
     d += (Rf := Resistor(  d='right', l=d.unit*1, label=R2label))
     d += ( Dot())
     d += ( Line( d='up',xy=Rf.start, l=d.unit/2))
     d += (Cout:= Capacitor(  d='right', l=d.unit*1, label=Clabel))
     d += ( Line( d='down', toy=op.out))
     d += ( Dot())
     d += ( Line( d='left', tox=op.out))
     d += ( Line( d='right', l=d.unit/4))
     d += ( Dot(open=True,rgtlabel=voutlabel))
    return
    
    
def freqs_resp(ba_array,Dmin=1,Dmax=5,lowDB=-100, Npts = 1024,fsize=(6,4),legend=[],Printcoef=True,ShowGraf=True):
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
    if ShowGraf:
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
        if ShowGraf:
            w,H = signal.freqs(ba[0],ba[1],2*np.pi*f)
            if legend==[]:
                ax[0].semilogx(f,20*np.log10(np.abs(H)))
            else:
                ax[0].semilogx(f,20*np.log10(np.abs(H)),label=legend[index])
                index+=1
            ax[1].semilogx(f,np.angle(H)/np.pi*180)
    if ShowGraf:
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
        plt.show();
        
def polen_nullen(z,p,circelarray,fsize=(6,6),Printcoef=True,ShowGraf=True):
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
    if ShowGraf:
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