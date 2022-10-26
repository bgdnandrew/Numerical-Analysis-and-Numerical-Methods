import numpy as np
import matplotlib.pyplot as plt

# secant method with tolerance and approx. saved to list
def secant_method_2(f, x0, x1, tol):
    x2 = 0
    approx_list = []
    while abs(f(x2)) > tol:
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0 = x1
        x1 = x2
        approx_list.append(x2)
    return approx_list

# false position with tolerance and approx. saved to list
def false_position_method_2(f, x0, x1, tol):
    x2 = 0
    approx_list = []
    while abs(f(x2)) > tol:
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        approx_list.append(x2)
        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
    return approx_list

# ---
def f(x):
    return np.cos(x) - x

# ---
def custom_graph(f):
    x = np.linspace(0, np.pi/2, 100)
    y = f(x)

    plt.title("F and Approx. Chains")
    plt.axhline(y=0)
    plt.axvline(x=0)
    plt.xlim(0.0, 1.0) # x-axis range
    plt.ylim(-1.0, 1.0) # y-axis range
    plt.xlabel('x') 
    plt.ylabel('y') 
    plt.grid()

    plt.plot(x, y, color="black", label="F(x)")

    for approx in secant_method_2(f, 0, np.pi/2, 1e-6):
        plt.scatter(approx, f(approx), color="red")
    for approx in false_position_method_2(f, 0, np.pi/2, 1e-6):
        plt.scatter(approx, f(approx), color="blue")

    # show legend labels only once, based on color
    for legend_item in ["secant method errors"]:
        plt.scatter([], [], color="r", label=legend_item)
    for legend_item in ["false position method errors"]:
        plt.scatter([], [], color="b", label=legend_item)
    plt.legend(loc='upper right')
    
    plt.plot()
    plt.show()


# ---
# print("Secant Method Approx. List", secant_method_2(f, 0, np.pi/2, 1e-6))
# print("False Position Method Approx. List", false_position_method_2(f, np.pi/2, 0, 1e-6))
custom_graph(f)