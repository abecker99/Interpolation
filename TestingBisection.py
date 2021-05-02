import numpy as np


def find_sign_change(f, step, a, b):
    x = a
    pairs = []
    while (x + step < b):
        if (f(x + step)/f(x) < 0):
            pairs.append([x, x+step])
        x += step
    return pairs

def bisect(f, pairs, tolerance):
    zeros = []
    for pair in pairs:
        midpoint = (pair[1] - pair[0])/2 + pair[0]
        while (abs(f(midpoint)) > tolerance):
            if (f(midpoint)/f(pair[0]) < 0):
                pair[1] = midpoint
            else:
                pair[0] = midpoint
            midpoint = (pair[1] - pair[0])/2 + pair[0]
        max_iter = 1000
        zeros.append(midpoint)
    return zeros
#zeros are z, need to computer energy with it    
def sinc(x):
    if (x == 0):
        return 1
    else:
        return np.sin(x)/x

pairs = find_sign_change(sinc, 0.1, 0, 10)
print(pairs)
zeros = bisect(sinc, pairs, 1E-10)
print(zeros)
print(np.pi, 2.0*np.pi, 3.0*np.pi)