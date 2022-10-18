import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative


def newton_raphson_1(f, f_prime, x0, max_iter):
    x = x0
    print('x:', x)
    for i in range(max_iter):
        x_new = x - f(x)/f_prime(x)
        x = x_new
        print("Approx. number ", i+1, " is ", x)
    return x

# newton raphson that does not need f_prime as an argument
def newton_raphson_2(f, x0, max_iter):
    x = x0
    print('x:', x)
    for i in range(max_iter):
        x_new = x - f(x)/f_prime_maker(f, x)
        x = x_new
        print("Approx. number ", i+1, " is ", x)
    return x


def graph_maker_and_saver(f):
    x = np.linspace(-1, 1, 100)
    y = f(x)
    plt.plot(x, y)
    plt.grid()
    plt.savefig('graphf.eps', format='eps')
    plt.show()

def f_prime_maker(f, x):
    return derivative(f, x, dx=1e-6)


# ---------------------------------------------

def f(x):
    return x + np.exp(-x**2) * np.cos(x)

# we can omit the f_prime parameter for newton-raphson and compute it when we need it (newton_raphson_2)
# alternatively, this is the hardcoded f_prime
def f_prime(x):
    #return the derivative of f(x)
    return (np.exp(x**2)-2*x*np.cos(x)-np.sin(x)) / np.exp(x**2)


# ---------------------------------------------

# graph_maker_and_saver(f)
# print(newton_raphson_1(f, f_prime, 0, 10))
# print(newton_raphson_2(f, 0, 10))

