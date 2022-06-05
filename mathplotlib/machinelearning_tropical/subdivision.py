
import matplotlib.pyplot as plt
import numpy as np

def draw_polygon(ax, verts, only_edges=False, color='black'):
    ax.plot([v[0] for v in verts] + [verts[0][0]], [v[1] for v in verts] + [verts[0][1]], [v[2] for v in verts] + [verts[0][2]], color=color, solid_capstyle='butt')
    if not only_edges:
        for v in verts:
            ax.plot(*v, 'o', color=color)

def draw_line(ax, verts, color='black'):
    ax.plot([v[0] for v in verts], [v[1] for v in verts], [v[2] for v in verts], '--', color='.7',)


ax = plt.subplot2grid((1,2), (0,0), projection='3d')
ax2 = plt.subplot2grid((1,2), (0,1))

draw_line(ax, [[0, 0, -2], [0, 0, 0]])
draw_line(ax, [[2, 0, -2], [2, 0, 0]])
draw_line(ax, [[0, 2, -2], [0, 2, 0]])
draw_line(ax, [[1, 0, -2], [1, 0, 1]])
draw_line(ax, [[0, 1, -2], [0, 1, 1]])
draw_line(ax, [[1, 1, -2], [1, 1, 1]])

#ax.text(0, 0, -.2, "$(0,0,0)$", color='black')
#ax.text(2, 0, -.2, "$(2,0,0)$", color='black')
#ax.text(0, 2, -.2, "$(0,2,0)$", color='.7')
#ax.text(1, 0,  0.8, "$(1,0,1)$", color='black')
#ax.text(0, 1,  1.2, "$(0,1,1)$", color='black')
#ax.text(1, 1,  1.2, "$(1,1,1)$", color='black')

draw_polygon(ax, [[0, 0, 0], [2, 0, 0], [0, 2, 0]], color='.7')
draw_polygon(ax, [[1, 1, 1], [0, 1, 1], [0, 2, 0]], color='.7')
draw_polygon(ax, [[1, 0, 1], [0, 1, 1], [1, 1, 1]])
draw_polygon(ax, [[1, 1, 1], [2, 0, 0], [1, 0, 1]])
draw_polygon(ax, [[0, 0, 0], [1, 0, 1], [0, 1, 1]])
draw_polygon(ax, [[0, 0, 0], [2, 0, 0]])



draw_polygon(ax, [[0, 0, -2], [2, 0, -2], [0, 2, -2]], color='.7')
draw_polygon(ax, [[1, 0, -2], [0, 1, -2], [1, 1, -2]], color='.7')


ax.axis('off')
ax.set_xticks([]) 
ax.set_yticks([]) 
ax.set_zticks([])
ax.set_xlim(2/3 - 1, 2/3 + 1)
ax.set_ylim(2/3 - 1, 2/3 + 1)
ax.set_zlim(-0.5 - 1, 0.5 + 1)

ax.set_title('$P_f$')

def draw_polygon(ax, verts, only_edges=False, color='black'):
    ax.plot([v[0] for v in verts] + [verts[0][0]], [v[1] for v in verts] + [verts[0][1]], color=color, solid_capstyle='butt')
    if not only_edges:
        for v in verts:
            ax.plot(*v, 'o', color=color)

draw_polygon(ax2, [[0, 0], [2, 0], [0, 2]])
draw_polygon(ax2, [[1, 0], [0, 1], [1, 1]])
ax2.axis('equal')
ax2.axis('off')
ax2.set_title('Newt$(f)$')
ax2.set_xlim(-2, 4)
ax2.set_ylim(-2, 4)

#
#x2 = np.linspace(-3, 2, 100)
#y2 = np.maximum(0, x2)
#a2.plot(x2, y2)
#a2.set_title('ReLU')
#
#x3 = np.linspace(-3, 2, 100)
#y3 = np.maximum(x3/10, x3)
#a3.plot(x3, y3)
#a3.set_title('Leaky ReLU')

plt.show()
