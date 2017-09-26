from bqplot import *
from IPython.display import display

x_data = [2.5, 5, 10, 20, 30, 50]
opentrons_data = [106, 109, 147, 212, 276, 462]
echo_data = [105, 136,224,393, 566, 888]

x_sc = LinearScale(min=0)
y_sc = LinearScale(min=0)

ax_x = Axis(label='Volume', scale=x_sc, tick_format='0.0f')
ax_y = Axis(label='Time (seconds)', scale=y_sc, orientation='vertical', tick_format='0.0f')

line = Lines(x=x_data,
             y=opentrons_data,
             scales={'x': x_sc, 'y': y_sc},
             colors=['red', 'yellow'])

line2 = Lines(x=x_data,
             y=echo_data,
             scales={'x': x_sc, 'y': y_sc},
             colors=['green', 'green'])

fig = Figure(axes=[ax_x, ax_y], marks=[line,line2])

display(fig)
