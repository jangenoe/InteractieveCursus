* CIRCUIT Spice file van een verschilversterker
VDD    1 0 DC=5.0
VPLUS 10 0 DC=2.5
VMIN  11 0 SIN(2.5 50U 1E6) DC=2.5
VB    9 0 DC=1.5
C3     3 0   5.914fF
C4     4 0  14.737fF
C5     5 0  10.124fF
C6     6 0  14.434fF
C8     8 0   7.919fF
C9     9 0  15.257fF
C10   10 0 1.872fF
C11   11 0 1.688fF
C25    1 5  1fF
MN1 3 5 0 0  NMOS w=1.50u L=0.50u 
MN2 0 5 5 0  NMOS w=1.50u L=0.50u
MN3 8 10 4 0 NMOS w=1.50u L=0.50U
MN4 0 9 8 0  NMOS w=4.50u L=0.50U
MN5 6 11 8 0 NMOS w=1.50u L=0.50U 
MP1 1 4 3 1  PMOS w=3.50u L=0.50U
MP2 4 4 1 1  PMOS w=3.50u L=0.50U
MP3 1 6 5 1  PMOS w=3.50u L=0.50U
MP4 6 6 1 1  PMOS w=3.50u L=0.50U
.MODEL NMOS NMOS(LEVEL=1 VTO=0.50 KP=90.000E-6 LAMBDA=0.001)
.MODEL PMOS PMOS(LEVEL=1 VTO=-0.45 KP=55.000E-6 LAMBDA=0.001)