# Bogdan Andrei
# Rares Sburlan

# suport:
# http://ramanujan.math.trinity.edu/rdaileda/teach/s17/m3357/lectures/lecture9.pdf
# https://www.youtube.com/watch?v=ly4S0oi3Yz8&ab_channel=3Blue1Brown
# https://youtu.be/ToIXSwZ1pJU

# ∂u/∂t = α ∂²u/∂x²
# where u(x,t) is the temperature at position x and time t, α is the thermal diffusivity constant, 
# and ∂/∂x and ∂/∂t represent partial derivatives with respect to x and t, respectively. 
# This equation is used to model a variety of physical phenomena such as the flow of heat through a metal rod or the diffusion of heat through a fluid.

import numpy as np
import matplotlib.pyplot as plt
# import spsolve from scipy.sparse.linalg
# from scipy.sparse import diags

# Parameters
a = 0
b = 1
h = 0.01 
alpha = 0.01  # alpha=thermal diffusivity constant
T = 1  # timp
N = int((b - a) / h)  # noduri

x = np.linspace(a, b, N + 1)  # spatiu
t = np.linspace(0, T, N + 1)  # timp

u0 = np.sin(np.pi * x) # sinusoidala

A = np.zeros((N - 1, N - 1))

# A = diags([-alpha, 1+2*alpha, -alpha], [-1, 0, 1], shape=(N-2, N-2)).toarray()
# for i in range(1, len(t)):
#     b = u + alpha * (u0[2:] - 2 * u + u0[:-2]) / h ** 2
    

# umplem matricea
# for i in range(1, N - 1):
for i in range(1, N - 2):
    A[i, i] = 1 + 2 * alpha
    A[i, i - 1] = -alpha
    A[i, i + 1] = -alpha

u = u0[1:-1] 
for i in range(1, len(t)):
    b = u + alpha * (u0[2:] - 2 * u + u0[:-2]) / h ** 2
    u = np.linalg.solve(A, b)
    u0[1:-1] = u

#---
for i in range(1,4):
    h = h/2 # injumatatim pasul
    N = int((b - a) / h)
    x = np.linspace(a, b, N + 1)  #spatiu
    u0 = np.sin(np.pi * x)
    A = np.zeros((N - 1, N - 1))

    for i in range(1, N - 1):
        A[i, i] = 1 + 2 * alpha
        A[i, i - 1] = -alpha
        A[i, i + 1] = -alpha
    u = u0[1:-1] 
    for i in range(1, len(t)):
        b = u + alpha * (u0[2:] - 2 * u + u0[:-2]) /h ** 2
        u = np.linalg.solve(A, b)
        u0[1:-1] = u
    error = np.abs(np.sin(np.pi*x)-u0)
    plt.semilogy(x, error) # eroare pe scala logaritmica
    plt.xlabel('x')
    plt.ylabel('error')
    plt.legend()

plt.figure()
plt.plot(x, u0, label='Numerical')
plt.plot(x, np.sin(np.pi * x), label='Exact')

plt.xlabel('x')
plt.ylabel('u(x,t)')
plt.legend()
plt.show()

