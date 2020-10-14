import cfig
import numpy as np
import matplotlib.pyplot as plt

V = np.array([.05, .1, .15, .2, .5, 1])
A = np.array([320, 303, 290, 285, 261, 243])
A_sample = 307

fit = np.poly1d(np.polyfit(V, A, 1))

line_x = [0, 1]
plt.scatter(V, A, label='Standard Sample')
plt.scatter((fit-A_sample).r, A_sample, marker='x', c='g')
plt.plot(line_x, fit(line_x), c='r', label='Standard Curve')
plt.axhline(y=A_sample, ls="--", linewidth=1)
plt.xlabel(r"$c\,/\,\mathrm{\mu g\cdot mL^{-1}}$", fontsize=14)
plt.ylabel(r"$\rm{E\,/\,mV}$", fontsize=14)
plt.annotate('('+'%.2f'%((fit-A_sample).r)+', '+'%.3f'%A_sample+')',
             xy = ((fit-A_sample).r, A_sample+5), fontsize = 12)
plt.legend(fontsize=14, loc='lower left')

plt.show()