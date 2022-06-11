'''
Module in charge of drawing the subdivided Netwon polygon
'''

import numpy as np

from bokeh.models import Segment

def plot(plot, points, subdivision_ids, flat_edges):
    '''
    Given a list of points, draw the subdivided Newton polygon
    '''
    # plot the subdivision of the Newton polygon
    for simplex in subdivision_ids:
        for i in range(3):
            id1, id2 = simplex[i], simplex[(i+1) % 3]
            # skip flat edges ()
            if set([id1, id2]) in flat_edges:
                continue
            edge = np.array([points[id1], points[id2]])
            #ax.plot(edge[:,0], edge[:,1], color=config.COLOR)
            plot.segment(edge[0][0], edge[0][1], edge[1][0], edge[1][1])
            #ax.plot(points[id1][0], points[id1][1], 'o', color=config.COLOR)
