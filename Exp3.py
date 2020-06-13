import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

config = {
    "font.family":'serif',
    "mathtext.fontset":'stix',
    "font.serif": ['SimSun'],
    'figure.dpi':'140',
}
rcParams.update(config)
plt.rcParams['font.serif'] = ['Times New Roman']

k_01 = 1530
k_02 = 1587
t = np.array([4, 8, 12, 16, 20, 24, 28, 32, 36, 40])
kt_1 = np.array([1402, 1360, 1323, 1291, 1261, 1235, 1212, 1190, 1170, 1152])
kt_2 = np.array([1542, 1452, 1381, 1324, 1277, 1238, 1204, 1176, 1151, 1129])
t = t * 60
k_1 = (k_01 - kt_1)/t
k_2 = (k_02 - kt_2)/t


fit_1 = np.poly1d(np.polyfit(k_1[1:], kt_1[1:], 1))
fit_2 = np.poly1d(np.polyfit(k_2[1:], kt_2[1:], 1))
print('func_1=', fit_1)
print('func_2=', fit_2)

plt.xlabel(r'$\frac{\kappa_0-\kappa_{t}}{t}\mathrm{/\mu S\cdot cm^{-1}\cdot s^{-1}}$', fontsize=14)
plt.ylabel(r'$\kappa_{t}\mathrm{/\mu S\cdot cm^{-1}}$', fontsize=14)


line_x1 = [0.15, 0.5]
plt.scatter(k_1, kt_1, label='measuring data')
plt.plot(line_x1, fit_1(line_x1), c='r', label='$y=1072x+1004$')
print(k_1, kt_1)

line_x2 = [0.175, 0.3]
#plt.scatter(k_2, kt_2, label='measuring data')
#plt.plot(line_x2, fit_2(line_x2), c='r', label='$y=2945x+546.8$')
#print(k_2, kt_2)

plt.legend(fontsize=14, loc='lower right')

plt.show()