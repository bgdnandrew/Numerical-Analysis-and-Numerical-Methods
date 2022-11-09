import numpy as np
import matplotlib.pyplot as plt

# https://www.youtube.com/watch?v=BTYTj0r5PZE&t=354s&ab_channel=OscarVeliz
def aitken(f, x0, max_iter, tol):
    a0 = newton_raphson(f, f_prime, x0, 1)
    b0 = newton_raphson(f, f_prime, x0, 2)
    c0 = newton_raphson(f, f_prime, x0, 3)

    print('a0:', a0, 'b0:', b0, 'c0:', c0)

    forward_difference0 = b0 - a0
    second_order_central_difference0 = c0 - 2*b0 + a0

    p_hat = a0 - (forward_difference0**2)/(second_order_central_difference0)

    a = a0
    b = b0
    c = c0

    for i in range(max_iter-1):
        print("iteration #", i+1)
        a = b
        b = c
        c = newton_raphson(f, f_prime, x0, i+4)

        print("a#{}:".format(i+1), a, "b#{}:".format(i+1), b, "c#{}:".format(i+1), c) 

        forward_difference = b - a
        second_order_central_difference = c - 2*b + a

        print('forward_difference:', forward_difference, 'second_order_central_difference:', second_order_central_difference)

        p_hat = a - (forward_difference**2)/(second_order_central_difference)
        print("p_hat:", p_hat)

        if abs(p_hat - c)/abs(c) < tol:
            return p_hat 

    return p_hat

def steffensen(f, x0, max_iter, tol):
    a = x0
    b = newton_raphson(f, f_prime, a, 1)
    c = newton_raphson(f, f_prime, b, 1)

    print('a:', a, 'b:', b, 'c:', c)

    aux_nominator = b - a
    aux_denominator = a - 2*b + c

    p_hat = a - (aux_nominator**2)/(aux_denominator)

    for i in range(max_iter-1):
        print("iteration #", i+1)
        a = p_hat
        b = newton_raphson(f, f_prime, a, 1)
        c = newton_raphson(f, f_prime, b, 1)

        print("a#{}:".format(i+1), a, "b#{}:".format(i+1), b, "c#{}:".format(i+1), c) 

        aux_nominator = b - a
        aux_denominator = a - 2*b + c

        print('aux_nominator:', aux_nominator, 'aux_denominator:', aux_denominator)

        p_hat = a - (aux_nominator**2)/(aux_denominator)
        print("p_hat:", p_hat)

        if abs(p_hat - c)/abs(c) < tol:
            return p_hat 

    return p_hat


def newton_raphson(f, f_prime, x0, max_iter):
    x = x0
    # print('x:', x)
    for i in range(max_iter):
        x_new = x - f(x)/f_prime(x)
        x = x_new
        # print("Approx. number ", i+1, " is ", x)
    return x

def f(x):
    return x**3 - 4*x**2 + 5*x - 2

def f_prime(x):
    return 3*x**2 - 8*x + 5

# print(aitken(f, 1.7, 20, 1e-10))
# print(steffensen(f, 1.7, 20, 1e-10))
