import cfig
import numpy as np
import matplotlib.pyplot as plt
from Exp6_data import n_1, n_2, X_2

fit = np.poly1d(np.polyfit(X_2, n_2, 1))
gama = fit.deriv()/n_1
print("func = ", fit)
print("gama = ", gama)

line_x = [0, 0.35]

plt.scatter(X_2, n_2)
plt.plot(line_x, fit(line_x), c="r", label=r"$n_2=-0.06251X_2+1.426$")

plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel(r'$X_2\mathrm{/mol\cdot L^{-1}}$', fontsize=14)
plt.ylabel(r'$n_2$', fontsize=14)

plt.legend(fontsize=14)
plt.show()