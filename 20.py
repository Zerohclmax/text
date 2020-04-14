import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi,2*np.pi,200)##对+-2Π之间取200点
y=np.cos(x)
plt.scatter(x, y, color='black', marker='.')##背景是黑色，点是‘.’
plt.show()`