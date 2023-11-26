from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import warnings
import numpy
import re

f_str1 = input('Input first function:\n ')
f_str2 = input('Input second function:\n ')
init_nr = input('Input start number point:\n')


# validation of data
def input_validation(str1, str2, val):
    reg_ex = r'^[0-9\.\+\-\*/xX\*\*]+$'
    try:
        float(val)
        if re.match(reg_ex, str1) and re.match(reg_ex, str2):
            return True
        else:
            print('Invalid input expressions')
            return False

    except ValueError:
        print('Starting dot number must be int or float')
        return False


if input_validation(f_str1, f_str2, init_nr):
    # making expression from input string
    def func1(x): return eval(f_str1.lower())
    def func2(x): return eval(f_str2.lower())

    # x of expression
    def graph_cross(val):
        return func1(val) - func2(val)

    def graph_painting(cross_point):
        # graph limit(counting steps between dots, border limit)
        x = numpy.linspace(cross_point[0] - 10, cross_point[0] + 10, 100)

        # counting y's
        y1 = func1(x)
        y2 = func2(x)

        # painting graphs
        plt.figure()
        plt.title('Graph of 2 crossing functions')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.scatter(cross_point, func1(cross_point[0]), color='red', label='Crossing dot')
        plt.plot(x, y1, label=f'Function: {f_str1}')

        plt.plot(x, y2, label=f'Function: {f_str2}')
        plt.grid()
        plt.legend(loc='upper left')
        plt.show()


    def is_crossing(val):
        try:
            # searching for crossing point
            cross_point = fsolve(graph_cross, val)

            if func1(cross_point[0]) == func2(cross_point[0]):
                print(f'Crossing point is: X: {cross_point[0]:.2f} Y: {func1(cross_point[0]):.2f}\n')
                graph_painting(cross_point)
            else:
                print('No crossing points of functions')
        except RuntimeWarning:
            warnings.warn(str(RuntimeWarning))

    is_crossing(float(init_nr))
