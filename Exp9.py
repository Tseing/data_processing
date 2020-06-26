import cfig
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

filename = 'thermal data.txt'
temp, weig, heat = [], [], []

with open(filename, 'r', encoding='utf-8') as f:
    line = f.readlines()[2:]
    for i in range(len(line)):
        t, w, h = line[i].split()
        temp.append(float(t))
        weig.append(float(w))
        heat.append(float(h))

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(temp, weig, c='mediumseagreen')
ax2.plot(temp, heat, c='steelblue')

ax1.set_xlabel("Temperature(℃)")
ax1.set_ylabel("Weight(%)",c='mediumseagreen')
ax2.set_ylabel("Heat Flow(W/g)",c='steelblue')

ax2.plot([141, 535], [12.61, 12.61], c='black', linewidth=0.8)
ax2.annotate('',xy=(520, 3.05), xytext=(520, 12.75), arrowprops=dict(facecolor="r", arrowstyle="<->"))
ax2.annotate('59.24%',xy=(535, (3.05+12.75)/2))
 
plt.show()