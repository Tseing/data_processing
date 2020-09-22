import cfig
import numpy as np
import matplotlib.pyplot as plt

V = np.array([0, 0.5, 1.00, 2.00, 3.00, 4.00])
A = np.array([0, 3.813, 22.08, 45.99, 72.04, 96.77])
A_sample = 63.15
c = 10*V/25
print(c)

fit = np.poly1d(np.polyfit(c, A, 1))

line_x = [0, 2]
plt.scatter(c, A, label='Standard Sample')
plt.scatter((fit-A_sample).r, A_sample, marker='x', c='g')
plt.plot(line_x, fit(line_x), c='r', label='Standard Curve')
plt.axhline(y=A_sample, ls="--", linewidth=1)
plt.xlabel(r"$\rm{c} / mg\cdot L^{-1}$", fontsize=14)
plt.ylabel(r"$\rm{A}$", fontsize=14)
plt.annotate('('+'%.2f'%((fit-A_sample).r)+', '+'%.3f'%A_sample+')',
             xy = ((fit-A_sample).r, A_sample-8), fontsize = 12)
plt.legend(fontsize=14, loc='lower right')

plt.show()