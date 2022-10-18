import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative


# newton raphson with tolerance 
def newton_raphson_3(f, f_prime, x0, tol, max_iter):
    x = x0
    print("x0", x0) 
    for i in range(max_iter):
        print("i", i)
        x_new = x - f(x)/f_prime(x)
        print("x_new", x_new)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x

# newton raphson with tolerance and without f_prime as an argument
def newton_raphson_4(f, x0, tol, max_iter):
    x = x0
    print("x0", x0)
    for i in range(max_iter):
        print("i", i)
        x_new = x - f(x)/f_prime_maker(f, x)
        print("x_new", x_new)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x

# newton_raphson_4, results saved in a list
def newton_raphson_5(f, x0, tol, max_iter):
    x = x0
    print("x0", x0)
    x_list = []
    for i in range(max_iter):
        print("i", i)
        x_new = x - f(x)/f_prime_maker(f, x)
        print("x_new", x_new)
        x_list.append(x_new)
        if abs(x_new - x) < tol:
            return x_list
        x = x_new
    return x_list


def f_prime_maker(f, x):
    return derivative(f, x, dx=1e-6)

def custom_graph_maker(f, approx_list):
    x = np.linspace(0, np.pi/2, 100)
    y = f(x)
    plt.plot(x, y)
    plt.axhline(y=0, color='r', linestyle='-')
    for x in approx_list:
        plt.scatter(x, 0)
    plt.grid()
    plt.show()

# ---------------------------------------------

def f(x):
    return np.cos(x) - x

# again, we can omit the f_2_prime parameter for newton-raphson and compute it when we need it (newton_raphson_4)
# alternatively, this is the hardcoded f_prime
def f_prime(x):
    return -np.sin(x) - 1


# ---------------------------------------------

# print(newton_raphson_3(f, f_prime, np.pi/4, 1e-6, 10))
# print(newton_raphson_4(f, np.pi/4, 1e-6, 10))
# ---
custom_graph_maker(f, newton_raphson_5(f, np.pi/4, 1e-6, 10))
 