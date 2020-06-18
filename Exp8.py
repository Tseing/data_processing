import cfig
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

c = np.array([5, 3.33, 2.5, 2, 1.43])
#r = np.array([1.4687, 1.2533, 1.2163, 1.1593, 1.1135])
#sp = np.array([0.4687, 0.2533, 0.2163, 0.1593, 0.1135])

t0 = 89.14
t = np.array([149.50, 126.30, 115.38, 109.96, 103.66])
r = t/t0
sp = r - 1
print(sp)

rfit = np.poly1d(np.polyfit(c, np.log(r)/c, 1))
#spfit = np.poly1d(np.polyfit(c, sigma, 1))
line_x=[0,6]

plt.xlim(0, 6.5)
plt.scatter(c, np.log(r)/c)
#plt.scatter(c, np.log(sp)/c)
plt.plot(line_x, rfit(line_x), c='r')

plt.show()
