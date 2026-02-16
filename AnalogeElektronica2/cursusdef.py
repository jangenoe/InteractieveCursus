import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib import patches
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
from pygments import lexers, highlight
from pygments.formatters import HtmlFormatter
from myspicelexer import SpiceLexer
import os
os.environ['NGSPICE_LIBRARY_PATH'] = '/opt/homebrew/Cellar/libngspice/45.2/lib/libngspice.dylib'

usewidgets=False;

def spicelisting(filename,firstline=0,lastline=10000,name=None,caption=None):
    """Display SPICE listing with custom lexer highlighting"""
    ff=""
    with open(filename) as f:
        for i,line in enumerate(f):
            if i>=firstline and i<lastline:
                ff+=line.strip()+"\r"
    
    lexer = SpiceLexer()
    formatter = HtmlFormatter(cssclass='highlight spice')
    highlighted = highlight(ff, lexer, formatter)
    
    # Add inline CSS for Jupyter notebook compatibility - force dark theme
    inline_css = """
    <style>
    .highlight.spice {
        background-color: #1a202c !important;
        color: #e2e8f0 !important;
        border: 1px solid #4a5568 !important;
        border-radius: 6px;
        padding: 12px;
        font-family: 'SFMono-Regular', 'Monaco', 'Inconsolata', 'Roboto Mono', monospace;
        margin: 8px 0;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    }
    /* Force dark background and light text on ALL elements */
    .highlight.spice *,
    .highlight.spice pre,
    .highlight.spice code {
        background-color: transparent !important;
        color: #e2e8f0 !important;
    }
    /* Override JupyterLab theme variations specifically */
    html[data-theme="light"] .highlight.spice,
    html[data-jp-theme-light="true"] .highlight.spice,
    .jp-mod-light .highlight.spice {
        background-color: #1a202c !important;
        color: #e2e8f0 !important;
    }
    html[data-theme="light"] .highlight.spice *,
    html[data-jp-theme-light="true"] .highlight.spice *,
    .jp-mod-light .highlight.spice * {
        color: #e2e8f0 !important;
        background-color: transparent !important;
    }
    /* SPICE Token Colors - all with !important */
    .highlight.spice .c { color: #68d391 !important; font-style: italic; }
    .highlight.spice .k { color: #63b3ed !important; font-weight: bold; }
    .highlight.spice .o { color: #f6e05e !important; }
    .highlight.spice .n { color: #e2e8f0 !important; }
    .highlight.spice .nf { color: #81e6d9 !important; }
    .highlight.spice .m { color: #d6bcfa !important; }
    .highlight.spice .s { color: #9ae6b4 !important; }
    .highlight.spice .err { color: #f56565 !important; }
    .highlight.spice .x { color: #e2e8f0 !important; }
    .highlight.spice .nb { color: #63b3ed !important; }
    .highlight.spice .nc { color: #81e6d9 !important; font-weight: bold; }
    .highlight.spice .nn { color: #81e6d9 !important; }
    .highlight.spice .nt { color: #63b3ed !important; font-weight: bold; }
    .highlight.spice .nv { color: #e2e8f0 !important; }
    .highlight.spice .mi { color: #d6bcfa !important; }
    .highlight.spice .mf { color: #d6bcfa !important; }
    .highlight.spice .mh { color: #d6bcfa !important; }
    .highlight.spice .mo { color: #d6bcfa !important; }
    .highlight.spice .sb { color: #9ae6b4 !important; }
    .highlight.spice .sc { color: #9ae6b4 !important; }
    .highlight.spice .sd { color: #9ae6b4 !important; font-style: italic; }
    .highlight.spice .s2 { color: #9ae6b4 !important; }
    .highlight.spice .se { color: #d6bcfa !important; font-weight: bold; }
    .highlight.spice .sh { color: #9ae6b4 !important; }
    .highlight.spice .si { color: #9ae6b4 !important; }
    .highlight.spice .sr { color: #9ae6b4 !important; }
    .highlight.spice .s1 { color: #9ae6b4 !important; }
    </style>
    """
    
    return display.HTML(inline_css + highlighted)

def plotZ(Z, frequencies):
    """Plot complex impedance on a logarithmic frequency scale"""
    magnitude = np.abs(Z)
    phase = np.angle(Z) * 180/np.pi  # Convert to degrees
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    
    # Magnitude plot
    ax1.semilogx(frequencies, magnitude)
    ax1.set_ylabel('|Z| (Ω)')
    ax1.grid(True, which="both", ls="-", alpha=0.3)
    ax1.set_title('Impedance Magnitude')
    
    # Phase plot
    ax2.semilogx(frequencies, phase)
    ax2.set_xlabel('Frequency (Hz)')
    ax2.set_ylabel('∠Z (degrees)')
    ax2.grid(True, which="both", ls="-", alpha=0.3)
    ax2.set_title('Impedance Phase')
  


