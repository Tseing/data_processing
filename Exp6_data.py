import numpy as np

T = 25
X_2 = np.array([0.05, 0.10, 0.15, 0.20, 0.30])
n_2 = np.array([1.4233, 1.4201, 1.4168, 1.4140, 1.4076])
n_1 = 1.4246
rho_2 = np.array([0.7757, 0.7811, 0.7857, 0.7898, 0.7998])
rho_1 = 0.7800
C_2 = np.array([8.16, 8.79, 9.31, 10.00, 11.11])
C_1 = 7.58
C_0 = 4.85

eps_1 = 2.05-0.001*1.55*T
C_d = (C_1-eps_1*C_0)/(1-eps_1)
C_0 = C_0 - C_d
C_2 = C_2 - C_d

eps_2 = C_2/C_0