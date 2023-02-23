import matplotlib.pyplot as plt
import numpy as np

tp= np.array([52.5, 38.5, 34.07, 31.9, 31, 30.75, 30.9, 31.55, 32.2])
rp= np.array([5, 10, 15, 20, 25, 30, 35, 40, 45])

tn= np.array([54.25, 39.85, 34.5, 31.9, 30.95, 30.35, 30.85, 31.35, 32])
rn= np.array([-5, -10, -15, -20, -25, -30, -35, -40, -45])

plt.scatter(rp, tp, 10)
plt.scatter(rn, tn, 10)

x1= np.arange(-45,43)
x2= np.arange(-36.5,35.5)

plt.plot(rp,tp, "red")
plt.plot(rn,tn, "green")


plt.text(-45,32.5,"A(-45,32)",size=10,color="blue")
plt.text(-17,32.5,"B(-20,32)",size=10,color="blue")
plt.text(0.5,32.5,"C(0,32)",size=10,color="blue")
plt.text(20,32.5,"D(20,32)",size=10,color="blue")
plt.text(43,32.5,"E(43,32)",size=10,color="blue")

plt.text(-45, 29.5, "A'(-36.5,31)", size=10, color="blue")
plt.text(-24, 29.5, "B'(-25,31)", size=10, color="blue")
plt.text(0.5, 29.5, "C'(0,31)", size=10, color="blue")
plt.text(19, 29.5, "D'(24.5,31)", size=10, color="blue")
plt.text(38, 29.5, "E'(35.5,31)", size=10, color="blue")


xm= np.array([-45,-20,0,20,43])
ym= np.array([32,32,32,32,32])

xs= np.array([-36.5,-25,0,24.5,35.5])
ys =np.array([31,31,31,31,31])

plt.scatter(xm, ym)
plt.scatter(xs,ys)

plt.plot(x1, 0*x1+32, "black")
plt.plot(x2, 0*x2+31, "black")

plt.grid()

plt.show()