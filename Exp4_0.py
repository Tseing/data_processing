import cfig
import numpy as np
import matplotlib.pyplot as plt
from Exp4_data import t, a_t, a_inf

fit = np.poly1d(np.polyfit(t, a_t, 5))
print(a_t-a_inf)

line_x=np.arange(-5, 65, 0.01)

plt.scatter(t, a_t)
plt.plot(line_x, fit(line_x), c='r')

plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel(r'$t\mathrm{/\min}$', fontsize=14)
plt.ylabel(r'$\alpha_t\mathrm{/\;^\circ}$', fontsize=14)

plt.show()