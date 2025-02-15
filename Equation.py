import matplotlib.pyplot as plt
import numpy as np
import math

def f(x, a):

    if a == 1:
        return x ** 3 - x + 1

    elif a == 2:
        return x ** 3 - x ** 2 - 9 * x + 9

    elif a == 3:
        return x ** 2 - np.e ** x

    elif a == 4:
        return 5 * x - 6 * math.log(x, np.e) - 7

    elif a == 5:
        return np.cos(x) + 2 * x - 3


def divider(x1, x2, e, a):
    global mid

    if a > 5 or a < 1:
        return 'Error'

    while abs(x1 - x2) >= e:
        mid = (x1 + x2) / 2

        if f(x1, a) * f(mid, a) <= 0:
            x2 = mid

        elif f(x2, a) * f(mid, a) <= 0:
            x1 = mid

        else:
            return 'None'
    return mid

a = 1

while a != 0:
    a = int(input('What equation do you want to solve (from 1 to 5)? '))
    x1 = float(input('First border: '))
    x2 = float(input('Second border: '))
    e = float(input('Accuracy: '))
    print(f"Equation's {a} solution on interval [{x1}, {x2}] is:", divider(x1, x2, e, a))
    fig, ax = plt.subplots()

