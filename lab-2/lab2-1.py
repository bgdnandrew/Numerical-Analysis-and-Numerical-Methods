import numpy as np
import matplotlib.pyplot as plt
from numpy import sqrt
from scipy.misc import derivative

def fixed_point(f, x0, max_iter):
    x = x0
    print('x:', x)
    for i in range(max_iter):
        print('i', i)
        x_new = f(x)
        print('x_new:', x_new) 
        x = x_new
    return x

def graph_maker(f):
    x = np.linspace(1, 2, 100)
    y = f(x)
    plt.plot(x, y)
    plt.grid()
    plt.show()

def graph_maker_2(f_prime, f):
    x = np.linspace(1, 2, 100)
    y = abs(f_prime(f, x))
    plt.plot(x, y)
    plt.grid()
    plt.show()

def f_prime_maker(f, x):
    return derivative(f, x, dx=1e-6)

#---------------------------------------------

def f(x):
    return x**3 + 4*(x**2) - 10

def phi_1(x):
    return -(x**3)-4*(x**2)+x+10

def phi_2(x):
    return sqrt(10/x - 4*x)

def phi_3(x):
    return 0.5 * sqrt(10 - x**3)

def phi_4(x):
    return sqrt(10/(x+4))


# ---------------------------------------------
# print(fixed_point(f, 1.4, 5))
# ---
# TBD: observe if Brouwer's fixed point theorem is satisfied for the phi functions
# graph_maker(f)
# graph_maker(phi_1)
# graph_maker(phi_2)
# graph_maker(phi_3)
# graph_maker(phi_4)
# ---
# graph_maker_2(f_prime_maker, phi_1)
# graph_maker_2(f_prime_maker, phi_2)
# graph_maker_2(f_prime_maker, phi_3)
# graph_maker_2(f_prime_maker, phi_4)
# ---
# print("phi_1:", fixed_point(phi_1, 1, 20))
# print("phi_2:", fixed_point(phi_2, 1, 20))
# print("phi_3:", fixed_point(phi_3, 1, 20))
# print("phi_4:", fixed_point(phi_4, 1, 20))