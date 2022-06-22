import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np


ax1 = plt.subplot2grid((1,2),(0,0))
ax2 = plt.subplot2grid((1,2),(0,1))

# fig 1
# cubic
t = np.linspace(-1.7, 1.4, 100)
x = t**2 - 1
y = t*(t**2 - 1)
ax1.plot(x, y)

# line
x = np.linspace(-1.5, 2, 100)
y = -(np.sqrt(2)/2)*x - np.sqrt(2)/2
ax1.plot(x, y)

# intersection pts
ax1.plot([-1, -.5, 1], [0, -np.sqrt(2)/4, -np.sqrt(2)], 'ko',  markersize=4)

ax1.axis('equal')
ax1.set_xticks([]) 
ax1.set_yticks([])

# fig 2
# tropical cubic 
ax2.plot([+2,-0], [+2,-0], color='C0')
ax2.plot([-0,-0], [-0,-1], color='C0')
ax2.plot([-0,+1], [-1,-1], color='C0')
ax2.plot([+1,+2], [-1,-0], color='C0')
ax2.plot([+1,+1], [-1,-4], color='C0')
ax2.plot([-0,-1], [-1,-2], color='C0')
ax2.plot([-0,-1], [-0,-0], color='C0')
ax2.plot([-1,-1], [-0,+1], color='C0')
ax2.plot([-1,-0], [+1,+2], color='C0')
ax2.plot([-1,-4], [+1,+1], color='C0')
ax2.plot([-1,-2], [-0,-1], color='C0')
ax2.plot([-1,-1], [-2,-4], color='C0')
ax2.plot([-2,-4], [-1,-1], color='C0')
ax2.plot([-1,-2], [-2,-2], color='C0')
ax2.plot([-2,-2], [-1,-2], color='C0')
ax2.plot([-2,-3], [-2,-3], color='C0')
ax2.plot([-3,-3], [-3,-4], color='C0')
ax2.plot([-3,-4], [-3,-3], color='C0')

# tropical line
ax2.plot([-.75,    2], [-1.5, 1.25], color='orange')
ax2.plot([-.75,-0.75], [-1.5,   -4], color='orange')
ax2.plot([-.75,   -4], [-1.5, -1.5], color='orange')

# intersection pts
ax2.plot([-2, -.75, 0], [-1.5, -1.75, -.75], 'ko',  markersize=4)

ax2.axis('equal')
ax2.set_xticks([]) 
ax2.set_yticks([])

plt.show()
