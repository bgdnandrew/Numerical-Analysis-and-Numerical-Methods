import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative


# newton raphson with m = multiplication order 
def newton_raphson_m(f, f_prime, x0, tol, max_iter, m):
    x = x0
    i = 0
    print("x0", x0) 
    for i in range(max_iter):
        print("iteration #", i+1)
        x_new = x - m*f(x)/f_prime(x)
        print("x_new", x_new)
        if abs(x - x_new)/abs(x) < tol:
            return x_new, i+1
        x = x_new
    return x, i+1

# newton raphson unknown multiplication order with scipy's derivative
# doesn't work

# def newton_raphson_m_2(f, f_prime, x0, tol, max_iter):
#     x = x0
#     i = 0
#     print("x0", x0) 
#     for i in range(max_iter):
#         print("iteration #", i+1)
#         # denominator = the derivative of [f_(x) - f_prime(x)]
#         denominator = derivative(n_r_m_2_aux, x, dx=1e-6)
#         x_new = x - (f(x)/f_prime(x))/denominator
#         print("x_new", x_new)
#         if abs(x - x_new)/abs(x) < tol:
#             return x_new, i+1
#         x = x_new
#     return x, i+1

# newton raphson unknown multiplication order with hardcoded denominator
def newton_raphson_m_3(f, f_prime, x0, tol, max_iter):
    x = x0
    i = 0
    print("x0", x0) 
    for i in range(max_iter):
        print("iteration #", i+1)
        x_new = x - (f(x)/f_prime(x))/(1 - f(x)/f_prime(x)**2) # (f/g)' where g = f_prime(x)
        print("x_new", x_new)
        if abs(x - x_new)/abs(x) < tol:
            return x_new, i+1
        x = x_new
    return x, i+1

# ---
# used for the comparison function
# newton raphson with m = multiplication order, with a different stopping criterion and no intermediate prints
# avoids zero division error 
def newton_r_1(f, f_prime, x0, tol, max_iter, m):
    x = x0
    i = 0
    for i in range(max_iter):
        x_new = x - m*f(x)/f_prime(x)
        if abs(x_new - x) < tol:
            return x_new, i+1
        x = x_new
    return x, i+1

# used for the comparison function
# newton raphson unknown multiplication order with hardcoded denominator, with a different stopping criterion and no intermediate prints
# avoids zero division error 
def newton_r_2(f, f_prime, x0, tol, max_iter):
    x = x0
    i = 0
    for i in range(max_iter):
        x_new = x - (f(x)/f_prime(x))/(1 - f(x)/f_prime(x)**2) # (f/g)' where g = f_prime(x)
        if abs(x_new - x) < tol:
            return x_new, i+1
        x = x_new
    return x, i+1

# newton raphson with tolerance from lab 2
def newton_raphson(f, f_prime, x0, tol, max_iter):
    x = x0
    for i in range(max_iter):
        x_new = x - f(x)/f_prime(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x

def compare_implementations(f, f_prime, x0, tol, max_iter, m):
    print("N-R m known")
    print("iteration #", "N-R m known", "ErrAbs", "ErrRel", "|f(xn)|", "TOL")
    i = 0
    for i in range(max_iter):
        if i>0:
            err_abs = abs(newton_r_1(f, f_prime, x0, tol, i-1, m)[0] - newton_r_1(f, f_prime, x0, tol, i, m)[0])
            if abs(newton_r_1(f, f_prime, x0, tol, i-1, m)[0]) != 0:
                err_rel = err_abs/abs(newton_r_1(f, f_prime, x0, tol, i-1, m)[0])
            else: err_rel = "undefined"
        else:
            err_abs = "N/A"
            err_rel = "N/A"

        print(i+1,
            newton_r_1(f, f_prime, x0, tol, max(1, i), m)[0],
            err_abs,
            err_rel,
            abs(f(newton_r_1(f, f_prime, x0, tol, i, m)[0])),
            tol
        )

    print("------------------")

    print("N-R m unknown")
    print("iteration #", "N-R m unknown", "ErrAbs", "ErrRel", "|f(xn)|", "TOL")
    i = 0
    for i in range(max_iter):
        if i>0:
            err_abs = abs(newton_r_2(f, f_prime, x0, tol, i-1)[0] - newton_r_2(f, f_prime, x0, tol, i)[0])
            if abs(newton_r_2(f, f_prime, x0, tol, i-1)[0]) != 0:
                err_rel = err_abs/abs(newton_r_2(f, f_prime, x0, tol, i-1)[0])
            else: err_rel = "undefined"
        else:
            err_abs = "N/A"
            err_rel = "N/A"

        print(i+1,
            newton_r_2(f, f_prime, x0, tol, max(1, i))[0],
            err_abs,
            err_rel,
            abs(f(newton_r_2(f, f_prime, x0, tol, i)[0])),
            tol
        )

    print("------------------")

    print("N-R standard")
    print("iteration #", "N-R Standard", "ErrAbs", "ErrRel", "|f(xn)|", "TOL")
    i = 0
    for i in range(max_iter):
        if i>0:
            err_abs = abs(newton_raphson(f, f_prime, x0, tol, i-1) - newton_raphson(f, f_prime, x0, tol, i))
            if abs(newton_raphson(f, f_prime, x0, tol, i-1)) != 0:
                err_rel = err_abs/abs(newton_raphson(f, f_prime, x0, tol, i-1))
            else: err_rel = "undefined"
        else:
            err_abs = "N/A"
            err_rel = "N/A"
        print(i+1,
            newton_raphson(f, f_prime, x0, tol, max(1, i)),
            err_abs,
            err_rel,
            abs(f(newton_raphson(f, f_prime, x0, tol, i))),
            tol
        )

    print("------------------")


    

def graph_maker_and_saver(f, f_prime):
    plt.title("f(x) and f'(x)")
    plt.grid()

    x = np.linspace(0, 1.75, 100)
    y = f(x)
    plt.plot(x, y, label="f(x)", color="red")
    y = f_prime(x)
    plt.plot(x, y, label="f'(x)", color="blue")

    plt.legend(loc="upper left")

    plt.savefig('lab-4/graph-f-f-prime-4.eps', format='eps')
    plt.show()

def f(x):
    return x**3 - 4*x**2 + 5*x - 2

def f_prime(x):
    return 3*x**2 - 8*x + 5

def n_r_m_2_aux(x):
    return f(x)/derivative(f_prime, x, dx=1e-6)

# graph_maker_and_saver(f, f_prime)
# print(newton_raphson_m(f, f_prime, 1.5, 1e-10, 20, 2))
# print(newton_raphson_m_2(f, f_prime, 1.5, 1e-10, 20))
# print(newton_raphson_m_3(f, f_prime, 1.5, 1e-10, 45))
compare_implementations(f, f_prime, 0, 1e-10, 20, 3)
