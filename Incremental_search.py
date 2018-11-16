"Incremental seach method"
import math
import numpy as np


def incremental_seach(f, a, b, dx):
    """

    :param f: function
    :param a: int
    :param b: int
    :param dx: float
    :return: float, int
    """
    fa = f(a)
    c = a + dx
    fc = f(c)
    n = 1

    while np.sign(fa) == np.sign(fc):
        if a >= b:
            return a - dx, n

        a = c
        fa = fc
        c = a + dx
        fc = f(c)
        n += 1

    if fa == 0:
        return a, n
    elif fc == 0:
        return c, n
    else:
        return (a + c)/2., n


def first_f(x):
    return math.pow(x, 3) + 2 * math.pow(x, 2) - 5


x = incremental_seach(first_f, 2, 5, 7)
print("x-axis of the root: " + str(x[0]))
print("number of iterations used: " + str(x[1]))
