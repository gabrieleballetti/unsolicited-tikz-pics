import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np

a1 = plt.subplot2grid((1,2),(0,0))
a2 = plt.subplot2grid((1,2),(0,1))

el1 = Ellipse((.5, .5), width=1, height=.6, angle=0, edgecolor='green', fc='None', lw=1)
el2 = Ellipse((.7, .5), width=.4, height=.9, angle=0, edgecolor='orange', fc='None', lw=1)
a1.add_patch(el1)
a1.add_patch(el2)
a1.plot(.55, .799, .1, color='k')
a1.plot(.8803, .6947, .1, color='k')
a1.axis('equal')
a1.set_xticks([]) 
a1.set_yticks([]) 


a2.plot([-2, 0], [0, 0], color='green')
a2.plot([0, 0], [-2, 0], color='green')
a2.plot([0, 1], [0, 1], color='green')
a2.plot([1, 3], [1, 1], color='green')
a2.plot([1, 1], [1, 3], color='green')
a2.plot([3, 3], [1, -2], color='green')
a2.plot([1, -2], [3, 3], color='green')
a2.plot([1, 5], [3, 7], color='green')
a2.plot([3, 5.5], [1, 3.5], color='green')


a2.plot([-2,  0 + .5], [ 0 + 2,  0 + 2], color='orange')
a2.plot([0  + .5,  0 + .5], [-2,  0 + 2], color='orange')
a2.plot([0  + .5,  1 + .5], [ 0 + 2,  1 + 2],  color='orange')
a2.plot([1  + .5,  3 + .5], [ 1 + 2,  1 + 2],  color='orange')
a2.plot([1  + .5,  1 + .5], [ 1 + 2,  3 + 2],  color='orange')
a2.plot([3  + .5,  3 + .5], [ 1 + 2, -2], color='orange')
a2.plot([1  + .5, -2], [ 3 + 2,  3 + 2], color='orange')
a2.plot([1  + .5,  3 + .5], [ 3 + 2,  5 + 2],  color='orange')
a2.plot([3  + .5,  5 + .5], [ 1 + 2,  3 + 2],  color='orange')

a2.plot

a2.axis('equal')
a1.set_xticks([]) 
a1.set_yticks([]) 

plt.show()
