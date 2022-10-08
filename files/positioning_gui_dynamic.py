from textwrap import fill
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from trilateration import geometry as geo
from trilateration.math import *
import pandas as pd
from trilateration.math import get_intersect, easy_least_squares
from trilateration.geometry import Trilateration, Circle, Point

fig, ax = plt.subplots()

"""circ = []
f = open("tpod_conf.txt", "r")
for i in f:
    x, y, r = i.split()
    circ.append(plt.Circle((x,y), r, color='b', fill=False))
    plt.scatter(x, y, color='k', marker='x', s=50)
    ax.add_patch(circ[-1])"""

""""
d1 = 20

plt.scatter(0, 0, color = 'k', marker = 'x', s = 50)
plt.scatter(10, 0, color = 'r', marker = 'x', s = 50)
plt.scatter(d1, 0, color = 'k', marker = 'x', s = 50)
plt.scatter(10, 10, color = 'k', marker = 'x', s = 50)



ax.set_aspect('equal', adjustable='datalim')
ax.plot()   #Causes an autoscale update.
plt.title(" 2D Positioning System")
plt.xlabel(" X - Axis")
plt.ylabel(" Y - Axis")
plt.grid(True)
plt.show()"""

plt.ion()
plt.style.use('fivethirtyeight')     #  >:(

def animate(i):
    data = pd.read_csv('dynamic_data.csv') 

    df1 = data[data['Anchor'] == "0x1f2dc"]
    df2 = data[data['Anchor'] == "0x1f084"]
    df3 = data[data['Anchor'] == "0x1ebee"]

    offset_1 = 4.1
    offset_2 = 5.3
    offset_3 = 3.9

    dis_1 = (df1["Distance"].iloc(-1) / 100) - offset_1
    dis_2 = (df2["Distance"].iloc[-1] / 100) - offset_2
    dis_3 = (df3["Distance"].iloc[-1] / 100) - offset_3


    #dis_1 = (df1["Distance"] / 100) - offset_1
    #dis_2 = (df2["Distance"] / 100) - offset_2
    #dis_3 = (df3["Distance"] / 100) - offset_3

    print(dis_1, dis_2, dis_3)

    ax = plt.gca()

    C1 = Circle(0,0,dis_1)
    C2 = Circle(12,0,dis_2)
    C3 = Circle(6,10,dis_3)
    cp = easy_least_squares((C1,C2,C3))
    cp_x = cp.center.x
    cp_y = cp.center.y
    cp_r = cp.radius

    cir = plt.Circle((0, 0), dis_1, color='b',fill=False)
    cir2 = plt.Circle((12, 0), dis_2, color='b',fill=False)
    cir3 = plt.Circle((6, 10), dis_3, color='b',fill=False)
    cir4 = plt.Circle((cp_x, cp_y), cp_r, color='r',fill=False)

    plt.scatter(0, 0, color = 'k', marker = 'x', s = 50)
    plt.scatter(12, 0, color = 'k', marker = 'x', s = 50)
    plt.scatter(6, 10, color = 'k', marker = 'x', s = 50)
    plt.scatter(cp_x, cp_y, color = 'r', marker = 'x', s = 50)

    ax.add_patch(cir)
    ax.add_patch(cir2)
    ax.add_patch(cir3)
    ax.add_patch(cir4)
    ax.set_aspect('equal', adjustable='datalim')
    ax.plot()   #Causes an autoscale update.
    plt.title(" 2D Positioning System")
    plt.xlabel(" X - Axis")
    plt.ylabel(" Y - Axis")

while True:
    
    ani = FuncAnimation(plt.gcf(), animate, interval=1000)
    
    plt.legend()
    plt.tight_layout()
    plt.pause(1) # Number of seconds you wait to update the plot
    plt.savefig('test.png')
