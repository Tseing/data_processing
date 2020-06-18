import cfig
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

c = np.array([5, 3.33, 2.5, 2, 1.43])
t0 = 89.14
t = np.array([149.50, 126.30, 115.38, 109.96, 103.66])
r = t/t0
sp = r - 1

rfit = np.poly1d(np.polyfit(c, np.log(r)/c, 1))
spfit = np.poly1d(np.polyfit(c, sp/c, 1))
print("rfit = ", rfit)
print("spfit = ", spfit)
line_x=[0,6.5]

plt.xlim(0, 6.5)
plt.xlabel(r'$c\mathrm{/kg\cdot m^{-3}}$', fontsize=14)
plt.ylabel(r'$\frac{\eta_r}{c}\ \ $or$\ \ \ln{\frac{\eta_{sp}}{c}}$', fontsize=14)
plt.scatter(c, np.log(r)/c)
plt.scatter(c, sp/c)
plt.plot(line_x, rfit(line_x), label=r"$\frac{\eta_r}{c}=-0.0004739c+0.1057$")
plt.plot(line_x, spfit(line_x), label=r"$\ln{\frac{\eta_{sp}}{c}}=0.006198c+0.1041$")

plt.legend(fontsize=14)
plt.show()
