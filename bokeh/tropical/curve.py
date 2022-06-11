'''
Module in charge of drawing the tropical curve
'''

import numpy as np
import config

EPSILON = 1e-09

def plot(ax, points, subdivision_ids, flat_edges, use_min_convention=True):
    '''
    Given a list of points and a calculated hull, plot the tropical curve they
    define in a given subplot
    '''
    vertices = set()
    edge_to_vert = {}
    edge_to_third_pt ={}

    # draw the inner part
    for simplex in subdivision_ids:
        verts = np.take(points, simplex, 0)
        b = -verts[:, 2]
        A = np.append(verts[:, :2], -np.ones((3,1)), axis=1)
        x = np.linalg.solve(A, b)[:2]
        vertices.add(tuple(x))
        ax.plot(x[0], x[1], 'o', color=config.COLOR)
        ax.axis('equal')
        for i in range(3):
            edge = frozenset([simplex[i], simplex[(i+1) % 3]])
            if edge in flat_edges:
                continue
            if edge in edge_to_vert:
                x2 = edge_to_vert[edge]
                edge_to_vert.pop(edge)
                edge_to_third_pt.pop(edge)
                ax.plot([x[0], x2[0]], [x[1], x2[1]], color=config.COLOR)
            else:
                edge_to_vert[edge] = x
                edge_to_third_pt[edge] = simplex[(i+2) % 3]

    # find bounding box, used to decide length of the tentacles (lazy way, don't judge)
    box_min = np.full(2, float('inf'))
    box_max = np.full(2, float('-inf'))
    for p in vertices:
        box_min = np.minimum(box_min, p)
        box_max = np.maximum(box_max, p)

    # estend bounding box to improve visibility
    box_dim = box_max - box_min
    box_min -= np.maximum(
        box_dim * config.TENTACLE_MIN_RELATIVE_LENGTH,
        np.full(2, config.TENTACLE_MIN_ABSOLUT_LENGTH)
    )
    box_max += np.maximum(
        box_dim * config.TENTACLE_MIN_RELATIVE_LENGTH,
        np.full(2, config.TENTACLE_MIN_ABSOLUT_LENGTH)
    )

    # draw the tentacles
    for edge, vert in edge_to_vert.items():
        # find the direction
        edge_pts = np.take(points, list(edge), 0)[:, :2]
        edge_dir = edge_pts[1] - edge_pts[0]
        normal = np.array([-edge_dir[1], edge_dir[0]])
        normal = normal/np.linalg.norm(normal)

        # check that the edge normal points externally
        outer_vec = edge_pts[0] - points[int(edge_to_third_pt[edge])][:2]
        normal *= 1 if np.dot(normal, outer_vec) > 0 else -1
        normal *= -1 if use_min_convention else 1

        # clip tentacle to limits
        t_x = ((box_max[0] if normal[0] >= 0 else box_min[0]) - vert[0]) / normal[0] \
            if abs(normal[0]) > EPSILON else float('inf')
        t_y = ((box_max[1] if normal[1] >= 0 else box_min[1]) - vert[1]) / normal[1] \
            if abs(normal[1]) > EPSILON else float('inf')
        end = vert + min(t_x, t_y)*normal

        ax.plot([vert[0], end[0]], [vert[1], end[1]], color=config.COLOR)
