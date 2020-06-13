import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from  Exp7_data import c, n, lquin, sol

config = {
    "font.family":'serif',
    "mathtext.fontset":'stix',
    "font.serif": ['SimSun'],
    'figure.dpi':'140',
}
rcParams.update(config)
plt.rcParams['font.serif'] = ['Times New Roman']


fit = np.poly1d(np.polyfit(c, n, 1))
#sol = np.poly1d(np.polyfit(n, c, 1))
print('func = ', fit)
print('func = ', sol)
line_x = [0, 10]

plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel('$c\mathrm{/mol\cdot L^{-1}}$', fontsize=14)
plt.ylabel('$n$', fontsize=14)
plt.scatter(c, n, label='standard sample')
plt.scatter(sol(lquin), lquin, marker='^', label='solution sample')
for i in range(len(lquin)):
    plt.annotate('(%.4f, %.4f)'%(sol(lquin)[i], lquin[i]), xy=(sol(lquin)[i], lquin[i]-0.0016))

plt.plot(line_x, fit(line_x), c='r', label='$y=0.003012x+1.332$')

plt.legend(fontsize=14)
plt.show()