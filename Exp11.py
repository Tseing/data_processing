import cfig
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy.optimize import curve_fit


fig,subs=plt.subplots(2,2)
plt.subplots_adjust(wspace=0.25)


#[0][0]
wave_length = np.array(np.arange(560, 435, -5))
A_0 = np.array([.111, .143, .189, .247, .311, .381, .454, .514,
              .557, .580, .585, .577, .565, .553, .545, .539, 
              .542,.532, .512, .491, .472, .449, .435, .419, .404])
fit_0 = np.poly1d(np.polyfit(wave_length, A_0, 8))

line_x0 = np.arange(440, 560, 1)
subs[0][0].scatter(wave_length, A_0, 15)
subs[0][0].plot(line_x0, fit_0(line_x0), c='r', label='Absorption Curve')
subs[0][0].set_xlabel(r'$\lambda\mathrm{\,/\,nm}$', fontsize=10, labelpad=0)
subs[0][0].set_ylabel(r'$\mathrm{A}$', fontsize=10, labelpad=0)
subs[0][0].tick_params(axis='x',labelsize=10, pad=2, direction='in')
subs[0][0].annotate(r'$\lambda_{max}=510\,\mathrm{nm}$', xy =(519, 0.57), fontsize = 10)
subs[0][0].legend(fontsize=8)


#[0][1]
V_1 = np.array([.1, 2, 5, 10, 15, 20])
A_1 = np.array([.274, .291, .274, .263, .211, .298])
pH = 14 + np.log10(0.1*V_1/50)

subs[0][1].scatter(pH, A_1, 15)
subs[0][1].plot(pH, A_1, c='r')
subs[0][1].set_xlabel(r"$\rm{pH}$", fontsize=10, labelpad=0)
subs[0][1].set_ylabel(r"$\rm{A}$", fontsize=10, labelpad=0)
subs[0][1].tick_params(axis='x',labelsize=10, pad=2, direction='in')
subs[0][1].locator_params("x", nbins=10)
subs[0][1].xaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
subs[0][1].yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))


#[1][0]
def func(x, a, b, c):
    return a * np.exp(-b * x) + c

V_2 = np.array([.1, .2, .3, .5, 1, 2, 4])
A_2 = np.array([.134, .165, .263, .463, .596, .589, .597])

popt, pcov = curve_fit(func, V_2, A_2)
line_x2 = np.arange(0.1, 4.3, 0.1)
subs[1][0].scatter(V_2, A_2, 15)
subs[1][0].plot(line_x2, func(line_x2, *popt), c='r')
#plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
subs[1][0].set_xlabel(r'$V_R\,\mathrm{/\,mL}$', fontsize=10, labelpad=0)
subs[1][0].set_ylabel(r'$\mathrm{A}$', fontsize=10, labelpad=0)
subs[1][0].tick_params(axis='x',labelsize=10, pad=2, direction='in')
subs[1][0].xaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))


#[1][1]
V_3 = np.array([1, 2, 4, 6, 8, 10])
A_3 = np.array([.116, .190, .403, .678, .895, 1.148])
A_sample = 0.292
c_3 = 100*V_3/25

fit_3 = np.poly1d(np.polyfit(c_3, A_3, 1))
line_x3 = [3, 42]
subs[1][1].scatter(c_3, A_3, 15, label='Standard Sample')
subs[1][1].scatter((fit_3-A_sample).r, A_sample, marker='x', c='g')
subs[1][1].plot(line_x3, fit_3(line_x3), c='r', label='Standard Curve')
subs[1][1].axhline(y=A_sample, ls="--", linewidth=1)
subs[1][1].set_xlabel(r"$c\,/\,\mathrm{mg\cdot L^{-1}}$", fontsize=10, labelpad=0)
subs[1][1].set_ylabel(r"$\rm{A}$", fontsize=10, labelpad=0)
subs[1][1].annotate('$('+'%.2f'%((fit_3-A_sample).r)+', '+'%.3f'%A_sample+')$',
             xy = ((fit_3-A_sample).r, A_sample-0.12), fontsize = 10)
subs[1][1].tick_params(axis='x',labelsize=10, pad=2, direction='in')
subs[1][1].locator_params("y", nbins=6)
subs[1][1].xaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
subs[1][1].yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
subs[1][1].legend(fontsize=8)

plt.savefig("fig_out.png", dpi=400)
plt.show()