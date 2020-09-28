import cfig
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy.optimize import curve_fit

def func(x, a, b, c):
    return a * np.exp(-b * x) + c

V = np.array([.1, .2, .3, .5, 1, 2, 4])
A = np.array([.134, .165, .263, .463, .596, .589, .597])

popt, pcov = curve_fit(func, V, A)

line_x = np.arange(0.1, 4.3, 0.1)
plt.scatter(V, A)
plt.plot(line_x, func(line_x, *popt), c='r')
plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
plt.xlabel(r'$V_R\,\mathrm{/\,mL}$', fontsize=14)
plt.ylabel(r'$\mathrm{A}$', fontsize=14)

plt.show()