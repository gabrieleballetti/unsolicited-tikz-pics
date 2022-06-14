from os import remove
import numpy as np

from bokeh.io import curdoc, show
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Slider, TextInput, Range1d, CustomJS, Button, TextAreaInput
from bokeh.plotting import figure, output_file, show

from bokeh.io import show
from bokeh.models import CustomJS, TextAreaInput

from tropical import hull
from tropical import subdivision

from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import matplotlib.pyplot as plt
import numpy as np

def parse(string):
    '''
    Parse points from the textarea
    '''
    print(string)
    points = []
    for line in iter(string.splitlines()):
        point = [float(n) for n in line.split()]
        if len(point) == 3:
            points.append(point)
    print(points)
    return points

def preprocess_points(points, use_min_convention):
    '''
    Add a dummy point to avoid "flat" configurations
    '''
    sign = 1 if use_min_convention else -1
    new_pt = [points[0][0], points[0][1], points[0][2] + sign]
    points.append(new_pt)
    return np.array(points)

def draw_newton_poly(points):
    subdivision_ids, flat_edges = hull.compute_lu_hull(points, use_min_convention)
    edges = subdivision.edges(points, subdivision_ids, flat_edges)
    for edge in edges:
        fig.segment(edge[0][0], edge[0][1], edge[1][0], edge[1][1])

def update_limits(points):
    for p in points:
        min_x = min(min_x, p[0])
        max_x = max(max_x, p[0])
        min_y = min(min_y, p[1])
        max_y = max(max_y, p[1])

use_min_convention = False

# file to save the model
output_file("gfg.html")

# Set up plot
fig = figure(height=400, width=400, match_aspect=True)

default_points = """\
0 0 0
1 0 2
2 0 2
3 0 0
0 1 2
1 1 3
2 1 2
0 2 2
1 2 2
0 3 0
"""

textarea = TextAreaInput(title="Exponents + coefficients", value=default_points, height=400, width=300, sizing_mode="stretch_height")
button = Button(label='Click me', button_type="success")

min_x = 0
max_x = 0
min_y = 0
max_y = 0

def change_click():
    fig.renderers = []
    points = preprocess_points(parse(textarea.value), use_min_convention)
    draw_newton_poly(points)
    #update_limits(points)

button.on_click(change_click)


# preprocessing

fig.toolbar.logo = None
fig.toolbar_location = None
fig.axis.visible = False
fig.toolbar.active_drag = None
fig.toolbar.active_scroll = None
fig.toolbar.active_tap = None


fig.x_range=Range1d(min_x - 1, max_x + 1)
fig.y_range=Range1d(min_y - 1, max_y + 1)

inputs = column(textarea, button)
curdoc().add_root(row(inputs, fig))


change_click()