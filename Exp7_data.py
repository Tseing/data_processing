import numpy as np


std = np.array([1.0535, 2.1140, 3.0582, 4.4850, 5.7937, 6.3979, 7.5026, 8.5997])
n = np.array([1.3352, 1.3375, 1.3416, 1.3465, 1.3489, 1.3505, 1.3552, 1.3576])
lquin = np.array([1.3352, 1.3369, 1.3392, 1.3409, 1.3433, 1.3465, 1.3489])
sol = np.poly1d(np.polyfit(n, std, 1))
c = sol(lquin)

p = np.array([0.259, 0.243, 0.228, 0.212, 0.199, 0.188, 0.177])
p = p
K = 71.79/376
sigma = p * K

fit = np.poly1d(np.polyfit(c, sigma, 2))
df = fit.deriv()
gama = -df(c)*c/(8.314*298)