from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html
import numpy as np 

plot = figure(plot_width=500,plot_height=250)
plot.circle([0.1,0.2,0.3], [0.3,0.2,0.1], size=20, color="navy", alpha=0.5)
html = file_html(plot, CDN, "my plot")

f = open('plot.html','w')
f.write(html)
f.close()