.TITLE Ideal Transmission Line Example
V1 1 0 PULSE(0 1 0.1n 0.1n 0.1n 100n 200n)
Rs 1 2 30
O1 2 0 3 0 LOSSYMOD TD=2n
RL 3 0 120
.model LOSSYMOD ltra r=0.0514 g=0 l=615E-9 c=246e-12 len=0.0812