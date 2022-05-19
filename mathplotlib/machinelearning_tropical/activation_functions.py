import matplotlib.pyplot as plt
import numpy as np

a1 = plt.subplot2grid((1,3),(0,0))
a2 = plt.subplot2grid((1,3),(0,1), sharey=a1)
a3 = plt.subplot2grid((1,3),(0,2), sharey=a1)

x1 = np.linspace(-5, 5, 100)
y1 = 1/(1 + np.exp(-x1))
a1.plot(x1, y1)
a1.set_title('sigmoid')
a1.set_ylim([-.9, 2.9])

x2 = np.linspace(-3, 2, 100)
y2 = np.maximum(0, x2)
a2.plot(x2, y2)
a2.set_title('ReLU')

x3 = np.linspace(-3, 2, 100)
y3 = np.maximum(x3/10, x3)
a3.plot(x3, y3)
a3.set_title('Leaky ReLU')

plt.show()
