'''
Module in charge of drawing the subdivided Netwon polygon
'''

import numpy as np

from bokeh.models import Segment

def edges(points, subdivision_ids, flat_edges):
    edges = []
    # plot the subdivision of the Newton polygon
    for simplex in subdivision_ids:
        for i in range(3):
            id1, id2 = simplex[i], simplex[(i+1) % 3]
            # skip flat edges ()
            if set([id1, id2]) in flat_edges:
                continue
            edge = np.array([points[id1], points[id2]])
            edges.append(edge)
    return edges
