''' Present an interactive function explorer with slider widgets.
Scrub the sliders to change the properties of the ``sin`` curve, or
type into the title text box to update the title of the plot.
Use the ``bokeh serve`` command to run the example by executing:
    bokeh serve sliders.py
at your command prompt. Then navigate to the URL
    http://localhost:5006/sliders
in your browser.
'''
import numpy as np

from bokeh.io import curdoc, show
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Slider, TextInput, Range1d, CustomJS, TextAreaInput
from bokeh.plotting import figure, output_file, show

from bokeh.io import show
from bokeh.models import CustomJS, TextAreaInput

from tropical import hull
from tropical import subdivision

from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import matplotlib.pyplot as plt
import numpy as np

def parse(filename):
    '''
    Parse points from the input files
    '''
    file = open(filename, 'r', encoding="utf-8")
    points = []
    for line in file:
        point = [float(n) for n in line.split()]
        if len(point) == 3:
            points.append(point)
    file.close()
    return points

def preprocess_points(points, use_min_convention):
    '''
    Add a dummy point to avoid "flat" configurations
    '''
    sign = 1 if use_min_convention else -1
    new_pt = [points[0][0], points[0][1], points[0][2] + sign]
    points.append(new_pt)
    return np.array(points)

use_min_convention = False

# file to save the model
output_file("gfg.html")

# Set up plot
fig = figure(height=400, width=400, match_aspect=True)

list_points = [[0,0,0],[1,0,0],[0,1,0]]
# preprocessing
points = preprocess_points(list_points, use_min_convention)
subdivision_ids, flat_edges = hull.compute_lu_hull(points, use_min_convention)

subdivision.plot(fig, points, subdivision_ids, flat_edges)
fig.toolbar.logo = None
fig.toolbar_location = None
fig.axis.visible = False
fig.x_range=Range1d(-1, 2)
fig.y_range=Range1d(-1, 2)
fig.toolbar.active_drag = None
fig.toolbar.active_scroll = None
fig.toolbar.active_tap = None
show(fig)


points = TextAreaInput(value="default", rows=6, title="Label:")
points.js_on_change("value", CustomJS(code="""
    console.log('text_area_input: value=' + this.value, this.toString())
"""))

show(points)
#
#
## Set up widgets
#text = TextInput(title="title", value='my sine wave')
#offset = Slider(title="offset", value=0.0, start=-5.0, end=5.0, step=0.1)
#amplitude = Slider(title="amplitude", value=1.0, start=-5.0, end=5.0, step=0.1)
#phase = Slider(title="phase", value=0.0, start=0.0, end=2*np.pi)
#freq = Slider(title="frequency", value=1.0, start=0.1, end=5.1, step=0.1)
#
#
## Set up callbacks
#def update_title(attrname, old, new):
#    plot.title.text = text.value
#
#text.on_change('value', update_title)
#
#def update_data(attrname, old, new):
#
#    # Get the current slider values
#    a = amplitude.value
#    b = offset.value
#    w = phase.value
#    k = freq.value
#
#    # Generate the new curve
#    x = np.linspace(0, 4*np.pi, N)
#    y = a*np.sin(k*x + w) + b
#
#    source.data = dict(x=x, y=y)
#
#for w in [offset, amplitude, phase, freq]:
#    w.on_change('value', update_data)
#
#
## Set up layouts and add to document
#inputs = column(text, offset, amplitude, phase, freq)
#
#curdoc().add_root(row(inputs, plot, width=800))
#curdoc().title = "Sliders"