import cfig
import numpy as np
import matplotlib.pyplot as plt

k_01 = 1530
k_02 = 1587
kinf_1 = 745
kinf_2 = 803
t = np.array([4, 8, 12, 16, 20, 24, 28, 32, 36, 40])
kt_1 = np.array([1402, 1360, 1323, 1291, 1261, 1235, 1212, 1190, 1170, 1152])
kt_2 = np.array([1542, 1452, 1381, 1324, 1277, 1238, 1204, 1176, 1151, 1129])
k_1 = (k_01 - kt_1)/(kt_1 - kinf_1)
k_2 = (k_02 - kt_2)/(kt_2 - kinf_2)

fit_1 = np.poly1d(np.polyfit(t, k_1, 1))
fit_2 = np.poly1d(np.polyfit(t, k_2, 1))
print('func_1=', fit_1)
print('func_2=', fit_2)
print(k_1)
print(k_2)

line_x = [0, 45]
plt.scatter(t, k_1, label=r'$T=298.15\mathrm{K}$')
plt.plot(line_x, fit_1(line_x),
         label=r'$\frac{\kappa_0-\kappa_t}{\kappa_t-\kappa_\infty}=0.02036t+0.1131$')
plt.scatter(t, k_2, label=r'$T=308.15\mathrm{K}$')
plt.plot(line_x, fit_2(line_x),
         label=r'$\frac{\kappa_0-\kappa_t}{\kappa_t-\kappa_\infty}=0.03733t+0.0911$')

plt.xlabel(r'$t\mathrm{/min}$', fontsize=14)
plt.ylabel(r'$\frac{\kappa_0-\kappa_t}{\kappa_t-\kappa_\infty}$', fontsize=14)

plt.legend(fontsize=13)
plt.show()