Klasse G versterker
*
* SUPPLY VOLTAGES
VPOS1 8 0 DC	+70
VNEG1 6 0 DC	-70V
VPOS2 5 0 DC	+20V
VNEG2 4 0 DC	-20V
*
*  input source
VS1 1 0	DC 0 SIN(0V 48VPEAK 10KHZ)
*
*  PUSH-PULL TRANSISTOR OUTPUT STAGE
Q1h 8 1 9 QNPN
Q1s 9 12 2 QNPN
Q2s 7 13 2 QPNP
Q2h 6 1 7 QPNP
*
Dpos 5 9 DNOM
Dneg 7 4 DNOM
*
*compensatie Vsat
Db1 1 12 DNOM
Db4 13 1 DNOM
*
* Load resistance
RL1 2 0	8
*
* DEVICE MODELS
.model QNPN NPN(BF=50)
.model QPNP PNP(BF=50)
.model DNOM D()