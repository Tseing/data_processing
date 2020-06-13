import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from Exp7_data import lquin, sol

config = {
    "font.family":'serif',
    "mathtext.fontset":'stix',
    "font.serif": ['SimSun'],
    'figure.dpi':'140',
}
rcParams.update(config)
plt.rcParams['font.serif'] = ['Times New Roman']

p = np.array([0.259, 0.243, 0.228, 0.212, 0.199, 0.188, 0.177])
p = p
K = 71.79/376
s = p * K

fit = np.poly1d(np.polyfit(sol(lquin), s, 2))
print('f(x) = ', fit)
print('df/dx = ',fit.deriv())
line_x = np.arange(0, 6, 0.005)

plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel('$c\mathrm{/mol\cdot L^{-1}}$', fontsize=14)
plt.ylabel('$\sigma \mathrm{/N\cdot m^{-1}}$', fontsize=14)

plt.scatter(sol(lquin), s)
plt.plot(line_x, fit(line_x), c='r')


plt.show()