import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import LightSource

def fun(x, y):
    return np.maximum(0, np.maximum(x, np.maximum(y, np.maximum(-1 + x + y, np.maximum(-3 + 2*x, -3 + 2*y)))))

plt.plot([-2, 0], [0, 0], color='black')
plt.plot([0, 0], [-2, 0], color='black')
plt.plot([0, 1], [0, 1], color='black')
plt.plot([1, 3], [1, 1], color='black')
plt.plot([1, 1], [1, 3], color='black')
plt.plot([3, 3], [1, -2], color='black')
plt.plot([1, -2], [3, 3], color='black')
plt.plot([1, 3], [3, 5], color='black')
plt.plot([3, 5], [1, 3], color='black')

plt.axis('equal')
plt.axis('off')

plt.show()