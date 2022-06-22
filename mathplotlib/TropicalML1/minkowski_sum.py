import numpy as np
import matplotlib.pyplot as plt

def translate(verts, point):
    return [[v[0] + point[0], v[1] + point[1]] for v in verts]

def draw_polygon(ax, verts, only_edges=False, color='black'):
    ax.plot([v[0] for v in verts] + [verts[0][0]], [v[1] for v in verts] + [verts[0][1]], color=color, solid_capstyle='butt')
    if not only_edges:
        for v in verts:
            ax.plot(*v, 'o', color=color)

a1 = plt.subplot2grid((1,3),(0,0))
a2 = plt.subplot2grid((1,3),(0,1), sharey=a1)
a3 = plt.subplot2grid((1,3),(0,2), sharey=a1)

square = [
    [0, 0],
    [1, 0],
    [1, 1],
    [0, 1]
]

triangle = [
    [-1, -1],
    [1, 0],
    [0, 1]
]

mink = [
    [-1, -1],
    [0, -1],
    [2, 0],
    [2, 1],
    [1, 2],
    [0, 2],
    [-1, 0]
]

draw_polygon(a1, square)
a1.set_title('$P$')
a1.axis('equal')
a1.axis('off')

draw_polygon(a2, translate(triangle, [0, 0.5]))
a2.set_title('$Q$')
a2.axis('equal')
a2.axis('off')


draw_polygon(a3, translate(triangle, [1, 0.6]), only_edges=True, color='0.95')
draw_polygon(a3, translate(triangle, [1, 0.8]), only_edges=True, color='0.90')
draw_polygon(a3, translate(triangle, [1, 1]), only_edges=True, color='0.85')
draw_polygon(a3, translate(triangle, [0.8, 1]), only_edges=True, color='0.80')
draw_polygon(a3, translate(triangle, [0.6, 1]), only_edges=True, color='0.75')
draw_polygon(a3, translate(triangle, [0.4, 1]), only_edges=True, color='0.70')
draw_polygon(a3, translate(triangle, [0.2, 1]), only_edges=True, color='0.65')
draw_polygon(a3, translate(triangle, [0, 1]), only_edges=True, color='0.60')

draw_polygon(a3, translate(square, [-1, -1]), only_edges=True, color='0.6')

draw_polygon(a3, mink)
a3.set_title('$P+Q$')
a3.axis('equal')
a3.axis('off')


#ax.annotate("$(0,0)$", (0, 0), xytext=(0, 0 - 0.2))
#ax.annotate("$(1,0)$", (1, 0), xytext=(1, 0 - 0.2))
#ax.annotate("$(2,1)$", (2, 1), xytext=(2, 1 - 0.2))
#ax.annotate("$(2,2)$", (2, 2), xytext=(2, 2 - 0.2))
#ax.annotate("$(1,2)$", (1, 2), xytext=(1, 2 - 0.2))
#ax.annotate("$(0,1)$", (0, 1), xytext=(0, 1 - 0.2))


plt.show()