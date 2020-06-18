import cfig
import numpy as np
import matplotlib.pyplot as plt
from Exp4_data import t, a_t, a_inf

ln = np.log(a_t - a_inf)
fit = np.poly1d(np.polyfit(t, ln, 1))
print('ln(a_t-a_inf) = ', ln)
print('func = ', fit)
line_x = [-3, 65]

plt.scatter(t , ln)
plt.plot(line_x, fit(line_x), c='r',
         label=r"$\ln{\left(\alpha_t-\alpha_\infty\right)}=-0.05759t+3.071$")
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel(r'$t\mathrm{/min}$', fontsize=14)
plt.ylabel(r'$\ln{\left(\alpha_t-\alpha_\infty\right)}$', fontsize=14)

plt.legend(fontsize=14)
plt.show()