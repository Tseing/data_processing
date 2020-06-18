import cfig
import numpy as np
import matplotlib.pyplot as plt
from Exp7_data import lquin, c, fit, df, gama, sigma

print('f(x) = ', fit)
print('df/dx = ',df)
line_x = np.arange(0, 6, 0.005)

plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel('$c\mathrm{/mol\cdot L^{-1}}$', fontsize=14)
plt.ylabel('$\sigma \mathrm{/N\cdot m^{-1}}$', fontsize=14)

plt.scatter(c, sigma)
plt.plot(line_x, fit(line_x), c='r', label='$y=0.00043x^{2}-0.006305x+0.05587$')
for i in range(len(lquin)):
    plt.annotate('(%.2f, %.4f)'%(c[i], sigma[i]), xy=(c[i]-1.1, sigma[i]-0.0013))
    print("f'(%f) = "%c[i], df(c[i]))
    print("Gama = ", gama[i])

plt.legend(fontsize=14)
plt.show()