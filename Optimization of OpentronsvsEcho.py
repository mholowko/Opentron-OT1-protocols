from scipy.optimize import curve_fit
from bqplot import *
from IPython.display import display

def func(x, a):
    return a * x

x_data = [2.5, 5, 10, 20, 30, 50]
original_data = [106, 109, 147, 212, 276, 462]

popt, pcov = curve_fit(func,x_data,original_data,p0=9)

fit_data = func(x_data,popt)

x_sc = LinearScale(min=0)
y_sc = LinearScale(min=0)

ax_x = Axis(label='Volume', scale=x_sc, tick_format='0.0f')
ax_y = Axis(label='Time (seconds)', scale=y_sc, orientation='vertical', tick_format='0.0f')

line = Lines(x=x_data,
             y=original_data,
             scales={'x': x_sc, 'y': y_sc},
             colors=['red', 'black'],
             labels = ['original'],
             labels_visibility = 'label',
             display_legend=True)

line2 = Lines(x=x_data,
             y=fit_data,
             scales={'x': x_sc, 'y': y_sc},
             colors=['green', 'black'],
             labels = ['fit'],
             line_style = 'dashed',
             display_legend=True)

fig = Figure(axes=[ax_x, ax_y], marks=[line,line2],legend_location='left')

display(fig)
