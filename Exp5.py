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


et = np.array([1, 2, 3, 4, 5])
ht = np.array([0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00, 2.25, 2.50, 2.75,
             3.00, 3.25, 3.50, 3.75, 4.00, 4.25, 4.50, 4.75, 5.00, 5.25, 5.50,
             5.75, 6.00, 6.25, 6.50, 6.75, 7.00, 7.25, 7.50, 7.75, 8.00, 8.25,
             8.50, 8.75, 9.00, 9.25])
ht = ht + 5
dt = et + 9.25 + 5
t = np.append(np.append(et, ht),dt)
ht = np.append(5, ht)

etem_1 = np.array([0.003, 0.006, 0.008, 0.011, 0.014])
dtem_1 = np.array([1.509, 1.513, 1.518, 1.522, 1.525])
htem_1 = np.array([0.092, 0.237, 0.422, 0.609, 0.786, 0.933, 1.056, 1.146, 1.215,
                 1.267, 1.307, 1.342, 1.368, 1.388, 1.405, 1.422, 1.432, 1.441,
                 1.451, 1.456, 1.463, 1.468, 1.474, 1.478, 1.481, 1.484, 1.487,
                 1.490, 1.492, 1.494, 1.497, 1.498, 1.501, 1.502, 1.502, 1.503,
                 1.505])
tem_1 = np.append(np.append(etem_1, htem_1), dtem_1)
htem_1 = np.append(etem_1[4],htem_1)

etem_2 = np.array([0.009, 0.018, 0.024, 0.032, 0.037])
dtem_2 = np.array([1.743, 1.749, 1.752, 1.756, 1.762])
htem_2 = np.array([0.107, 0.275, 0.489, 0.705, 0.911, 1.070, 1.200, 1.303, 1.389,
                 1.453, 1.502, 1.542, 1.576, 1.601, 1.621, 1.638, 1.654, 1.667,
                 1.675, 1.684, 1.691, 1.698, 1.703, 1.707, 1.713, 1.716, 1.719,
                 1.722, 1.726, 1.727, 1.729, 1.731, 1.733, 1.736, 1.737, 1.738,
                 1.739])
tem_2 = np.append(np.append(etem_2, htem_2), dtem_2)
htem_2 = np.append(etem_2[4],htem_2)

#sample_1
efit = np.poly1d(np.polyfit(et, etem_1, 1))
print("environment func = " ,efit)
dfit = np.poly1d(np.polyfit(dt, dtem_1, 1))
print("dissipation func = ",dfit)
hfit = np.poly1d(np.polyfit(ht, htem_1, 10))
print("heat func = ",hfit)

#sample_2
#efit = np.poly1d(np.polyfit(et, etem_2, 1))
#print("environment func = " ,efit)
#dfit = np.poly1d(np.polyfit(dt, dtem_2, 1))
#print("dissipation func = ",dfit)
#hfit = np.poly1d(np.polyfit(ht, htem_2, 10))
#print("heat func = ",hfit)

line_x = [0,20]


plt.plot(ht, hfit(ht), c='royalblue')
plt.plot(line_x, efit(line_x), c='royalblue')
plt.plot(line_x, dfit(line_x), c='royalblue')
plt.axhline(y=1.0, ls="--", linewidth=1)
plt.xlabel(r'$\mathrm{Time/s}$', fontsize=14)
plt.ylabel(r'$\Delta T\mathrm{/K}$', fontsize=14)


#sample_1
plt.scatter(t, tem_1, c='tomato', marker='o')
plt.axvline(x=6.64336, ls="--", linewidth=1)
plt.scatter(x=6.64336, y=1.0, marker='x', c='darkorange')
plt.scatter([6.64336, 6.64336],[0.01824, 1.47423], marker='D', c='r')
plt.annotate('(6.6434, 0.0182)',xy=(6.76, 0.06),fontsize = 12)
plt.annotate('(6.6434, 1.4742)',xy=(1.39, 1.36),fontsize = 12)


#sample_2
#plt.scatter(t, tem_2, c='tomato', marker='o')
#plt.axvline(x=6.39725, ls="--", linewidth=1)
#plt.scatter(x=6.39725, y=1.0, marker='x', c='darkorange')
#plt.scatter([6.39725, 6.39725],[0.04778, 1.70379], marker='D', c='r')
#plt.annotate('(6.3973, 0.0478)',xy=(6.69, 0.12),fontsize = 12)
#plt.annotate('(6.3973, 1.7038)',xy=(1.25, 1.57),fontsize = 12)

plt.show()