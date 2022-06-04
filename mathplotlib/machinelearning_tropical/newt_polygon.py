import numpy as np
import matplotlib.pyplot as plt

ax = plt.subplot()

ax.plot([0, 1, 2, 2, 1, 0, 0], [0, 0, 1, 2, 2, 1, 0], color='black')
ax.plot(0, 0, 'o', color='black')
ax.plot(1, 0, 'o', color='black')
ax.plot(2, 1, 'o', color='black')
ax.plot(2, 2, 'o', color='black')
ax.plot(1, 2, 'o', color='black')
ax.plot(0, 1, 'o', color='black')

ax.annotate("$(0,0)$", (0, 0), xytext=(0, 0 - 0.2))
ax.annotate("$(1,0)$", (1, 0), xytext=(1, 0 - 0.2))
ax.annotate("$(2,1)$", (2, 1), xytext=(2, 1 - 0.2))
ax.annotate("$(2,2)$", (2, 2), xytext=(2, 2 - 0.2))
ax.annotate("$(1,2)$", (1, 2), xytext=(1, 2 - 0.2))
ax.annotate("$(0,1)$", (0, 1), xytext=(0, 1 - 0.2))

ax.axis('equal')
ax.axis('off')

plt.show()