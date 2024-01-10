Complementaire Darlington met emitter degeneratie
*
*  PUSH-PULL TRANSISTOR OUTPUT STAGE
Q1 2 1 4 QNPN
Q2 0 2 3 QPNP
RED 4 0 100
R2 2 3 100
*
* DEVICE MODELS
.model QNPN	NPN(BF=50)
.model QPNP	PNP(BF=50)