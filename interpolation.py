import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

def langrange_interpolation(x, x_i, y_i):
    N = len(x_i)
    result = 0
    for i in range(0,N):
        product = 1
        for j in range(0,N):
            if (j != i):
                product = product*(x - x_i[j])/(x_i[i] - x_i[j])
        result = result + product*y_i[i]
    return result

def Gauss(x, mu, sigma):
    y=[]
    for x in x_g:
        G = (1/(np.sqrt(2*np.pi)*sigma))*np.exp((-(x-mu)**2)/(2*sigma**2))
        y.append(G)
    return y


x_g = np.linspace(-4, 4, num=1000)
x_a = np.linspace(-4,4, num=10)
y_a = np.array([-7,6,-1,11,18])

y_g = Gauss(x_a, 0, 1)
interpolation = langrange_interpolation(x_g, x_a, y_g)
cs = CubicSpline(x_a, )

y_c = cs(x_g)

def function(x):
    f = (x-2)**3 - 3.5*x + 8
    return f
    
print(cs(2), cs(9))
plt.plot(x_g, y_g)
plt.plot(x_g, interpolation)
plt.plot(x_g, y_c)
plt.show()
