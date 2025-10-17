* Sallen and Key Low pass filter
R1 1 2 10k
R2 2 3 10k
XOpAmp 3 4 8 9 4 8 opamp
C1 2 4 2.2nF
C2 3 0 1.1nF
Vin 0 1 0 SIN(0V 1VPEAK 10KHZ)
* SUPPLY VOLTAGES
VPOS 8 0 DC +2.5V
VNEG 9 0 DC -2.5V