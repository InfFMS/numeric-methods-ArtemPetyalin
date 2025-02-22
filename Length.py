import numpy as np
import matplotlib.pyplot as plt

a = int(input("What slide's length do you want to count? "))
x = np.linspace(0, np.pi, 1000)

def y(x, a):
    if a == 1:
        return np.cos(x)

    elif a == 2:
        return np.cos(x) + 0.1 * x ** 2

    elif a == 3:
        return np.tanh(x - np.pi / 2)

    elif a == 4:
        return -0.2 * (x - np.pi) ** 3 + 0.5 * (x - np.pi) ** 2 + 1

fig, ax = plt.subplots(figsize=(10, 10))
plt.plot(x, y(x, a))
l = 0
c = 0
i = 0

while c != 1000:
    l += ((np.pi / 1000) ** 2 + (y(i + np.pi / 1000, a) - y(i, a)) ** 2) ** 0.5
    c += 1
    i += np.pi / 1000

print("length equals: ", l)
plt.grid()
plt.show()

