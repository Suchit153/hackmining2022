from textwrap import fill
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from trilateration import geometry as geo
from trilateration.math import *

fig, ax = plt.subplots()

"""circ = []
f = open("tpod_conf.txt", "r")
for i in f:
    x, y, r = i.split()
    circ.append(plt.Circle((x,y), r, color='b', fill=False))
    plt.scatter(x, y, color='k', marker='x', s=50)
    ax.add_patch(circ[-1])"""



d1 = 20
r1 = 10
r2 = 10
r3 = 10
cir = plt.Circle((0, 0), r1, color='b',fill=False)
cir2 = plt.Circle((d1, 0), r2, color='b',fill=False)
cir3 = plt.Circle((10, 10), r3, color='b',fill=False)

plt.scatter(0, 0, color = 'k', marker = 'x', s = 50)
plt.scatter(10, 0, color = 'r', marker = 'x', s = 50)
plt.scatter(d1, 0, color = 'k', marker = 'x', s = 50)
plt.scatter(10, 10, color = 'k', marker = 'x', s = 50)

ax.add_patch(cir)
ax.add_patch(cir2)
ax.add_patch(cir3)

ax.set_aspect('equal', adjustable='datalim')
ax.plot()   #Causes an autoscale update.
plt.title(" 2D Positioning System")
plt.xlabel(" X - Axis")
plt.ylabel(" Y - Axis")
plt.grid(True)
plt.show()
