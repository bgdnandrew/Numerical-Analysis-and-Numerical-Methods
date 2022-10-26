import numpy as np
import matplotlib.pyplot as plt

# secant method with max iterations
def secant_method(f, x0, x1, max_iter):
    x2 = 0
    for i in range(max_iter):
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        print("x2 = ", x2)
        x0 = x1
        print("x0 = ", x0)
        x1 = x2
        print("Approx. number ", i+1, " is ", "x2 = ", x2)
        #relative error old approx. vs new approx. (x0 holds the value for the old approx. now)
        print("Relative error: ", abs(x0 - x2) / abs(x0))
        print("---")
    return x2

# false position without tolerance
def false_position_method(f, x0, x1, max_iter):
    x2 = 0
    relative_error = 0
    previous_approx = []
    for i in range(max_iter):
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        if i!=0:
            print("previous approx: ", previous_approx[-1])
            print("Approx. number #", i+1, " is ", "x2 = ", x2)
            relative_error = abs(previous_approx[-1] - x2) / abs(previous_approx[-1])
            print("Relative error: ", relative_error)
            print("---")
        else: 
            print("Approx. number #", i+1, " is ", "x2 = ", x2)
            print("---")
        if f(x0) * f(x2) < 0:
            x1 = x2
            previous_approx.append(x1)
        else:
            x0 = x2
            previous_approx.append(x0)
    return x2

# secant method with max iterations and approx. saved to list
def secant_method_save_to_list(f, x0, x1, max_iter):
    x2 = 0
    error_list = []
    for i in range(max_iter):
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        print("x2 = ", x2)
        x0 = x1
        print("x0 = ", x0)
        x1 = x2
        print("Approx. number ", i+1, " is ", "x2 = ", x2)
        #relative error old approx. vs new approx. (x0 holds the value for the old approx. now)
        print("Relative error: ", abs(x0 - x2) / abs(x0))
        error_list.append(abs(x0 - x2) / abs(x0))
        print("---")
    return error_list

# false position without tolerance and approx. saved to list
def false_position_method_save_to_list(f, x0, x1, max_iter):
    x2 = 0
    relative_error = 0
    previous_approx = []
    error_list = []
    for i in range(max_iter):
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        if i!=0:
            print("previous approx: ", previous_approx[-1])
            print("Approx. number #", i+1, " is ", "x2 = ", x2)
            relative_error = abs(previous_approx[-1] - x2) / abs(previous_approx[-1])
            print("Relative error: ", relative_error)
            error_list.append(relative_error)
            print("---")
        else: 
            print("Approx. number #", i+1, " is ", "x2 = ", x2)
            print("---")
        if f(x0) * f(x2) < 0:
            x1 = x2
            previous_approx.append(x1)
        else:
            x0 = x2
            previous_approx.append(x0)
    return error_list

# ---
def graph_maker_and_saver(f):
    x = np.linspace(-1, 1, 100)
    y = f(x)
    plt.plot(x, y)
    plt.grid()
    plt.savefig('graphf-3.eps', format='eps')
    plt.show()

def error_iter_graph_maker(f, error_list_secant, error_list_false_position):
    iter_number = 1
    for error in error_list_secant:
        plt.scatter(iter_number, error_list_secant[iter_number-1], color="r")
        iter_number += 1
    iter_number = 1
    for error in error_list_false_position:
        plt.scatter(iter_number, error_list_false_position[iter_number-1], color="b")
        iter_number += 1
    
    plt.title("Relative Error vs. Iteration number")
    plt.axhline(y=0, color='#323232')
    plt.axvline(x=0, color='#323232')

    # show legend labels only once, based on color
    for legend_item in ["secant method errors"]:
        plt.scatter([], [], color="r", label=legend_item)
    for legend_item in ["false position method errors"]:
        plt.scatter([], [], color="b", label=legend_item)
    plt.legend(loc='upper right')

    plt.grid()
    plt.show()

def f(x):
    return x + np.exp(-x**2) * np.cos(x)


# ---
# graph_maker_and_saver(f)

# secant_method(f, -1, 1, 10)
# false_position_method(f, 1, -1, 10)
error_iter_graph_maker(f, secant_method_save_to_list(f, -1, 1, 10), false_position_method_save_to_list(f, 1, -1, 10))
