import cfig
import numpy as np
import matplotlib.pyplot as plt
from Exp7_data import std, n, lquin, sol, c

fit = np.poly1d(np.polyfit(std, n, 1))
print('func = ', fit)
print('func = ', sol)
line_x = [0, 10]

plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel('$c\mathrm{/mol\cdot L^{-1}}$', fontsize=14)
plt.ylabel('$n$', fontsize=14)
plt.scatter(std, n, label='standard sample')
plt.scatter(c, lquin, marker='^', label='solution sample')
for i in range(len(lquin)):
    plt.annotate('(%.4f, %.4f)'%(c[i], lquin[i]), xy=(c[i], lquin[i]-0.0016))

plt.plot(line_x, fit(line_x), c='r', label='$y=0.003012x+1.332$')

plt.legend(fontsize=14)
plt.show()