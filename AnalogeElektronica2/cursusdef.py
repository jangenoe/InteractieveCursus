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

usewidgets=False;
from IPython import display

def spicelisting(filename,firstline=0,lastline=10000,name=None,caption=None):
    ff=""
    with open(filename) as f:
        for i,line in enumerate(f):
            if i>=firstline and i<lastline:
                ff+=line.strip()+"\r"
    return display.Code(data=ff, language='spice')  # DisplayObject(data=ff, metadata={"name":name,"caption":caption})

