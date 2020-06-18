import math
import cfig
import numpy as np
import matplotlib.pyplot as plt

def linear_regression(x, y):
    """
    linear regression function
    b=slope
    A=intercept
    """
    N = len(x)
    sumx = sum(x)
    sumy = sum(y)
    sumx2 = sum(x ** 2)
    sumxy = sum(x * y)
    A = np.mat([[N, sumx], [sumx, sumx2]])
    b = np.array([sumy, sumxy])
    return np.linalg.solve(A, b)

#original data
dp = np.array([-77.50, -74.67, -71.15, -66.77, -61.40, -54.80])
t = np.array([298, 303, 308, 313, 318, 323])
dp_0 = -85.24
p =dp - dp_0
print("p=",p)
ln_p = np.log(p)
t = 1/t
print("lnp=",ln_p,"\n1/t=",t)

#linear regression
X = np.array(t)
Y = np.array(ln_p)
b, k = linear_regression(X, Y)
_X = [0, 100]
_Y = [b + k * x for x in _X ]
#print(k,b)

plt.xlim(0.00285, 0.0034)
plt.ylim(1.5, 5)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel(r'$T^{-1}\mathrm{/K^{-1}}$', fontsize=14)
plt.ylabel(r'$\ln p-\ln 10^3$', fontsize=14)
plt.plot(_X, _Y, c='red', label=r'$y='+'%.4f'%(k)+'x'+'+%.4f'%(b)+'$')
plt.scatter(t, ln_p, label='measuring data')
plt.axhline(y=math.log(101.325), ls="--", linewidth=1)
plt.scatter(x=(math.log(101.325)-b)/k,y=math.log(101.325),marker='x', c='purple')
plt.annotate('('+'%.5f'%((math.log(101.325)-b)/k)+', '+'%.2f'%math.log(101.325)+')',
             xy = ((math.log(101.325)-b)/k+0.00001, math.log(101.325)+0.1),
             fontsize = 12)
plt.legend(fontsize=14)

plt.show()