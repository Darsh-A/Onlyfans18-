import matplotlib.pyplot as plt
import numpy as np

t2l= np.array([35.6,38.3,44.1,50.8,59.75,69.9,83.3,98.4,115.65])
l2= np.array([25,100,225,400,625,900,1225,1600,2025])

a,b = np.polyfit(l2,t2l,1)

plt.scatter(l2,t2l)
plt.plot(l2,a*l2+b)

plt.text(1, 90, 'm = ' + '{:.2f}'.format(a), size=14)
plt.text(1,85,'c = ' + '{:.2f}'.format(b), size=14)

plt.show()