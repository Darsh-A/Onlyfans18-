import matplotlib.pyplot as plt
import numpy as np

tp= np.array([52.5, 38.5, 34.07, 31.9, 31, 30.75, 30.9, 31.55, 32.2])
rp= np.array([5, 10, 15, 20, 25, 30, 35, 40, 45])

tn= np.array([54.25, 39.85, 34.5, 31.9, 30.95, 30.35, 30.85, 31.35, 32])
rn= np.array([-5, -10, -15, -20, -25, -30, -35, -40, -45])

plt.plot(rn,tn)
plt.plot(rp,tp)

plt.plot()

plt.grid()

plt.show()