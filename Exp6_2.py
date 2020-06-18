import cfig
import numpy as np
import matplotlib.pyplot as plt
from Exp6_data import eps_1, eps_2, X_2

fit = np.poly1d(np.polyfit(X_2, eps_2, 1))
alpha = fit.deriv()/eps_1
print("func = ", fit)
print("alpha = ", alpha)
print("eps_1 = ", eps_1)

line_x = [0, 0.35]

plt.scatter(X_2, eps_2)
plt.plot(line_x, fit(line_x), c="r", label=r"$\varepsilon_2=4.378X_2+2.012$")

plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel(r'$X_2\mathrm{/mol\cdot L^{-1}}$', fontsize=14)
plt.ylabel(r'$\varepsilon_2$', fontsize=14)

plt.legend(fontsize=14)
plt.show()