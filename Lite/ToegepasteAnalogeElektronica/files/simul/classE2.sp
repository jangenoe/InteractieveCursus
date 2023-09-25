* Class E amp 1
M_M1         2 1 0 0 FDB33N25 
L_L1         2 3  1000uH  
C_C1         2 0  4.78nF  
L_L2         4 5  24.93uH  
C_C2         2 4  6.04nF  
R_RL         5 0  14.88 
V_Vdd        3 0 12.5V
V_Vin        1 0 PULSE(0 9 1.05u 20n 20n 1.05u 2.10526u) DC=0
.model FDB33N25 VDMOS(Rg=3 Rd=40m Rs=27m Vto=5.35 Kp=35 lambda=.05 Cgdmax=1.1n Cgdmin=25p Cgs=1.7n Cjo=800p Is=7.94p Rb=7m mfg=Fairchild Vds=250 Ron=94m Qg=37n)