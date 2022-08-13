* Class E Tsai
V_Vdd        3 0  2V
M_SWn        0 11 10 0 nmos W=31580u L=0.35u
M_SWp        3 11 10 3 pmos W=500u L=0.35u
* stage 1
L_L1         3 6  0.37nH
L_L2         3 7  0.37nH
M_11         10 1 6 0 nmos W=980u L=0.35u
M_12         10 7 6 0 nmos W=980u L=0.35u
M_13         10 6 7 0 nmos W=980u L=0.35u
M_14         10 2 7 0 nmos W=980u L=0.35u
* stage 2
M_21         10 6 8 0 nmos W=3600u L=0.35u
M_22         10 9 8 0 nmos W=4800u L=0.35u
M_23         10 8 9 0 nmos W=4800u L=0.35u
M_24         10 7 9 0 nmos W=3600u L=0.35u
L_L3         3 8  0.37nH
L_L4         3 9  0.37nH
L_L5         8 4  0.8nH 
L_L6         9 5  0.8nH 
C_C1         4 5  5.1pF
* belasting
R_RL1        4 0  50 
R_RL2        5 0  50 
.include simul/berkeley35.lib