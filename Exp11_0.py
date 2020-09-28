import cfig
import numpy as np
import matplotlib.pyplot as plt

wave_length = np.array(np.arange(560, 435, -5))
A = np.array([.111, .143, .189, .247, .311, .381, .454, .514,
              .557, .580, .585, .577, .565, .553, .545, .539, 
              .542,.532, .512, .491, .472, .449, .435, .419, .404])

print(wave_length)
fit = np.poly1d(np.polyfit(wave_length, A, 8))

line_x=np.arange(440, 560, 1)
plt.scatter(wave_length, A)
plt.plot(line_x, fit(line_x), c='r', label='Absorption Curve')
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel(r'$\lambda\mathrm{\,/\,nm}$', fontsize=14)
plt.ylabel(r'$\mathrm{A}$', fontsize=14)
plt.annotate(r'$\lambda_{max}=510\,\mathrm{nm}$', xy =(520, 0.58), fontsize = 12)
plt.legend(fontsize=14)

plt.show()