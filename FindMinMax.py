import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(0.001, np.pi, 2000)
rx = 15
ry1 = 10
ry2 = 10
n1 = float(input("Refractive index of area 1: "))
n2 = float(input("Refractive index of area 2: "))
def L(a, n1, n2, rx, ry1, ry2):
    return np.sin(a) 
    #return n1 * (ry1 / np.sin(a)) + n2 * (((rx - (ry1 / np.sin(a))) ** 2 + ry2 ** 2) ** 0.5)

fig, axs = plt.subplots(1, 2, figsize=(10, 10))
axs[0].plot(a, L(a, n1, n2, rx, ry1, ry2))
plt.show()