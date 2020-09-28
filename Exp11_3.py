import cfig
import numpy as np
import matplotlib.pyplot as plt

V = np.array([1, 2, 4, 6, 8, 10])
A = np.array([.116, .190, .403, .678, .895, 1.148])
A_sample = 0.292
c = 100*V/25
print(c)

fit = np.poly1d(np.polyfit(c, A, 1))

line_x = [3, 42]
plt.scatter(c, A, label='Standard Sample')
plt.scatter((fit-A_sample).r, A_sample, marker='x', c='g')
plt.plot(line_x, fit(line_x), c='r', label='Standard Curve')
plt.axhline(y=A_sample, ls="--", linewidth=1)
plt.xlabel(r"$c\,/\,\mathrm{mg\cdot L^{-1}}$", fontsize=14)
plt.ylabel(r"$\rm{A}$", fontsize=14)
plt.annotate('('+'%.2f'%((fit-A_sample).r)+', '+'%.3f'%A_sample+')',
             xy = ((fit-A_sample).r, A_sample-0.1), fontsize = 12)
plt.legend(fontsize=14, loc='lower right')

plt.show()