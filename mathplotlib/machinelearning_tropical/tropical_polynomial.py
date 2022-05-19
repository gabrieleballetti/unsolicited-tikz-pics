import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LightSource

def fun(x, y):
    return np.maximum(0, np.maximum(x, np.maximum(y, np.maximum(-1 + x + y, np.maximum(-3 + 2*x, -3 + 2*y)))))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = y = np.arange(-2.0, 5.0, 0.05)
X, Y = np.meshgrid(x, y)
zs = np.array(fun(np.ravel(X), np.ravel(Y)))
Z = zs.reshape(X.shape)


l = LightSource(azdeg=315, altdeg=45, hsv_min_val=1, hsv_max_val=1, hsv_min_sat=1, hsv_max_sat=1)

ax.plot_surface(X, Y, Z, linewidth=0, antialiased=True, shade=True, lightsource=l, alpha=.9)

ax.set_xticks([]) 
ax.set_yticks([]) 
ax.set_zticks([])

ax.plot([-2, 0], [0, 0], [-3, -3], color='black')
ax.plot([0, 0], [-2, 0], [-3, -3], color='black')
ax.plot([0, 1], [0, 1],  [-3, -3], color='black')
ax.plot([1, 3], [1, 1],  [-3, -3], color='black')
ax.plot([1, 1], [1, 3],  [-3, -3], color='black')
ax.plot([3, 3], [1, -2], [-3, -3], color='black')
ax.plot([1, -2], [3, 3], [-3, -3], color='black')
ax.plot([1, 3], [3, 5],  [-3, -3], color='black')
ax.plot([3, 5], [1, 3],  [-3, -3], color='black')


plt.show()