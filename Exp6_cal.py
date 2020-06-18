import numpy as np
from Exp6_0 import gama
from Exp6_1 import beta
from Exp6_2 import alpha
from Exp6_data import n_1, rho_1, eps_1

M_1 = 84.16
M_2 = 88.11
T = 298.15

P = (3*alpha*eps_1*M_1)/((eps_1+2)**2*rho_1) + ((eps_1-1)*(M_2-beta*M_1))/((eps_1+2)*rho_1)

R = ((n_1**2-1)*(M_2-beta*M_1))/((n_1**2+2)*(rho_1)) + (6*n_1**2*M_1*gama)/((n_1+2)**2*rho_1)

m = 0.0426*np.sqrt((P-R)*T)

print("P = ", P)
print("R = ", R)
print("m = ", m, "*10^-30")