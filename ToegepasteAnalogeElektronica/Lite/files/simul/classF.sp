* klasse F basiscircuit
Q_Q1         2 1 0 Q2
L_L1         5 3   1uH  
C_C1         5 3   10n  
R_R1         5 3   60  
V_V3         3 0   11V
V_V5         1 0   sin(0.7 0.8 1591500) DC=0.7
C_C3         5 2   10n  
L_L3         5 2   0.111uH
.model Q2  NPN(Is=14.34f BF=200 RB=200 )