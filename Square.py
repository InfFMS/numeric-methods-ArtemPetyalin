import matplotlib.pyplot as plt
import numpy as np
import math

a = int(input("What blob's square do you want to count? "))

if a == 1:
    x = np.linspace(0, np.pi, 1000)

    def y1(x):
        return math.sin(2 * x) + 1

    def y2(x):
        return -0.2 * (x ** 2) + 0.5

    y1arr = np.array(np.sin(2 * x) + 1)
    y2arr = np.array(-0.2 * (x ** 2) + 0.5)

    fig, ax = plt.subplots(figsize=(10, 10))
    ax.plot(x, y1arr, label="y1")
    ax.plot(x, y2arr, label="y2")
    s1 = 0
    s2 = 0
    i = 0
    c = 0

    while c != 1000:
        s1 += (y1(i + np.pi / 1000) + y1(i)) / 2 * np.pi / 1000
        s2 += (y2(i + np.pi / 1000) + y2(i)) / 2 * np.pi / 1000
        i += np.pi / 1000
        c += 1

    s = s1 - s2

    plt.fill_between(x, y1arr, y2arr, color="blue", alpha=0.3)
    plt.grid(True)
    print("Square equals", s)
    plt.show()

elif a == 2:
    x = np.linspace(-2, 2, 1000)

    def y1(x):
        return np.e ** (-1 * x ** 2) + 1

    def y2(x):
        return -0.3 * x ** 2 + 0.5

    y1arr = np.array(np.e ** (-1 * x ** 2) + 1)
    y2arr = np.array(-0.3 * x ** 2 + 0.5)

    fig, ax = plt.subplots(figsize=(10, 10))
    ax.plot(x, y1arr, label="y1")
    ax.plot(x, y2arr, label="y2")
    s1 = 0
    s2 = 0
    i = -2
    c = 0

    while c != 1000:
        s1 += (y1(i + 4 / 1000) + y1(i)) / 2 * 4 / 1000
        s2 += (y2(i + 4 / 1000) + y2(i)) / 2 * 4 / 1000
        i += 4 / 1000
        c += 1

    s = s1 - s2

    plt.fill_between(x, y1arr, y2arr, color="blue", alpha=0.3)
    plt.grid(True)
    print("Square equals", s)
    plt.show()

