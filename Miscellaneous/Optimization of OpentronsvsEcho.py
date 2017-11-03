from scipy.optimize import curve_fit
from bqplot import *
from IPython.display import display
import math

opentrons_data = [106, 109, 147, 212, 276, 462]
echo_data = [105, 136,224,393, 566, 888]

List = [opentrons_data, echo_data]

def func(x, a, c, b):
    return (96 * a * x) + (c * 180/x) +  b 

for original_data in List:
    print (original_data)
    x_data = [2.5, 5, 10, 20, 30, 50]
    
    if original_data == opentrons_data:
        z=([0.,0.1,0.], [0.5,1.,1000.])
        
    elif original_data == echo_data:
        z=([0.,0.1,0.], [0.2,0.5,1000.])
    
    
    popt, pcov = curve_fit(func,x_data,original_data,bounds=z)
    popt = list(popt)
    print(popt)


    fit_data = []

    for x in x_data:
        fit_data.append(func(x,popt[0],popt[1],popt[2]))

    x_sc = LinearScale(min=0)
    y_sc = LinearScale(min=0)
    
    panzoom = PanZoom(scales={'x': [x_sc], 'y': [y_sc]})

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

    fig = Figure(axes=[ax_x, ax_y], marks=[line,line2],legend_location='left', interaction = panzoom)

    display(fig)
