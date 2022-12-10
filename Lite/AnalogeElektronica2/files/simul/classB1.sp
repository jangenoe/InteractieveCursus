Klasse B versterker
*
* SUPPLY VOLTAGES
VPOS 8 0 DC	+15V
VNEG 9 0 DC	-15V
*
*  input source
VS1 1 0	DC 0 SIN(0V 5VPEAK 10KHZ)
*
*  PUSH-PULL TRANSISTOR OUTPUT STAGE
Q1 8 1 2 QNPN
Q2 9 1 2 QPNP
*
* Load resistance
RL1 2 0	100
*
* DEVICE MODELS
.model QNPN	NPN(BF=50)
.model QPNP	PNP(BF=50)
