import cfig
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

V = np.array([.1, 2, 5, 10, 15, 20])
A = np.array([.274, .291, .274, .263, .211, .298])
pH = 14 + np.log10(0.1*V/50)
print(pH)


plt.scatter(pH, A)
plt.plot(pH, A, c='r')
plt.xlabel(r"$\rm{pH}$", fontsize=14)
plt.ylabel(r"$\rm{A}$", fontsize=14)
plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))

plt.show()