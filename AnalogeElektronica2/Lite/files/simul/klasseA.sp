* Spice file van een eenvoudige Klasse A versterker
R_R6         0 1  8  
R_R7         3 2  1  
L1_TX1       3 4 25m
L2_TX1       1 0 1m
K_TX1        L1_TX1 L2_TX1 1.
Q_Q5         4 5 0 Q2
I_I4         0 5  SIN(17m 15m 10k) DC=17m
V_VDD        2 0 66V

.model Q2  NPN(Is=14.34p BF=20 )