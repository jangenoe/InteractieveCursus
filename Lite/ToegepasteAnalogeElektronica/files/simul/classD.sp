* Class D amp 1
Q_Q1         3 1 2 Q2
Q_Qp         0 1 2 Qp
L_L1         5 2 1uH
C_C1         5 6 10n 
R_RL         6 0 6
V_Vdd        3 0 20V
R_Rin        4 1 1
V_Vin        4 0 PULSE(0 20 0 20ns 20ns 294ns 628ns) DC=0
.model Q2  NPN(Is=14.34f BF=200)
.model Qp  PNP(Is=5.34f BF=100)