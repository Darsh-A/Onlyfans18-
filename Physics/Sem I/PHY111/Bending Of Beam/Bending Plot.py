import numpy as np
import matplotlib.pyplot as plt

actualy = np.array([0, 0.5, 1, 1.5, 2, 2.5])
x = np.array([0, 0.001195, 0.002795, 0.00351, 0.00445, 0.005385])

print(actualy)

a, b = np.polyfit(x, actualy, 1)

plt.scatter(x, actualy)
plt.plot(x, a * x + b)

plt.show()
