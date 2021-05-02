import numpy as np
from scipy.interpolate import CubicSpline
from scipy.integrate import fixed_quad

def f(x):
    f = (x-2)**3 - 3.5*x + 8
    return f

def df(x):
    return df = 3*(x-2)**2-3.5

def int_f(x, a, b):
    upper = ((b-2.0)**4)/4-7*b**2/4.0 + 8.0*b
    lower = ((a-2.0)**4)/4-7*a**2/4.0 + 8.0*a
    return upper - lower

def central diff(f, x, h):
    return (f(x - h/ 2.0) - f(x-h)/2.0))/h

print(int_f(0,4,5))

f = function(x)
x = np.linspace(0,4,5)
y = f(x)

cs = CubicSpline(x,y)
result, err= fixed_quad(cs, 0.0,4.0,n=2)
print(result)
result, err - fixed_quad(f, 0.0,4.0,n=2)
print(result)

print(df(2.0),central_diff(cs,2.0,1E-6))
print(df(3.14159), central_diff(cs, 3.14159, 1E-6)), central_diff(f, 3.14159, 1E-6))
print(f(3.14159), cs(3.14159))