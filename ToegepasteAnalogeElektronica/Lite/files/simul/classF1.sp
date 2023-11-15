* klasseF basiscircuit
Q_Q1         2 1 0 Q2
L_L1         5 3   1uH  
C_C1         5 3   10n  
R_R1         5 3   60  
V_V3         3 0   11V
R_Rin        4 1   100
V_Vin        4 0   sin(-1.5 2.7 1591500) DC=-1.5
C_C3         5 2   10n  
L_L3         5 2   0.111uH  
.model Q2  NPN(Is=14.34f BF=200 BR=200)
