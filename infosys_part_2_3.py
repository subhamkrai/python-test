import numpy as np
import pandas as pd
from bokeh.io import output_file, show
from bokeh.models import HoverTool
from bokeh.plotting import figure


df = pd.read_csv('infosys.csv')

closing_price=df.Close
close = closing_price.tolist()

weeks=closing_price.rolling(window=260).mean()


n=len(weeks)
n1=len(close)


x = np.random.standard_normal(n)
y = np.random.standard_normal(n1)

p = figure(title="Hexbin for 500 points", match_aspect=True,
           tools="wheel_zoom,reset", background_fill_color='#440154')
p.grid.visible = False

r, bins = p.hexbin(x, y, size=0.5, hover_color="pink", hover_alpha=0.8)

p.circle(x, y, color="white", size=1)

p.add_tools(HoverTool(
    tooltips=[("count", "@c"), ("(q,r)", "(@q, @r)")],
    mode="mouse", point_policy="follow_mouse", renderers=[r]
))


show(p)
