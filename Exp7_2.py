import cfig
import numpy as np
import matplotlib.pyplot as plt
from Exp7_data import c, gama

fit = np.poly1d(np.polyfit(c, c/gama, 1))
print("func = ", fit)
print("limit Gama = ", 1/fit.deriv())

line_x=[1, 6]
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
ax = plt.gca()
ax.yaxis.get_major_formatter().set_powerlimits((0,1))
plt.xlabel(r'$c\mathrm{/mol\cdot L^{-1}}$', fontsize=14)
plt.ylabel(r'$\frac{c}{\Gamma}\mathrm{/10^{-3}m^{-1}}$', fontsize=14)
plt.scatter(c, c/gama)
plt.plot(line_x, fit(line_x), c='r', label='$y=251300x+34190$')
plt.legend(fontsize=14)
plt.show()