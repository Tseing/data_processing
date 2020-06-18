import cfig
import numpy as np
import matplotlib.pyplot as plt
from Exp6_data import rho_1, rho_2, X_2

fit = np.poly1d(np.polyfit(X_2, rho_2, 1))
beta = fit.deriv()/rho_1
print("func = ", fit)
print("beta = ", beta)

line_x = [0, 0.35]

plt.scatter(X_2, rho_2)
plt.plot(line_x, fit(line_x), c="r", label=r"$\rho_2=0.09497X_2+0.7712$")

plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel(r'$X_2\mathrm{/mol\cdot L^{-1}}$', fontsize=14)
plt.ylabel(r'$\rho_2\mathrm{/g\cdot cm^{-3}}$', fontsize=14)

plt.legend(fontsize=14)
plt.show()