import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import warnings
warnings.filterwarnings('ignore')
from bokeh.plotting import figure, output_file, show, output_notebook
import datetime

df = pd.read_csv('infosys.csv')

date_price=df.Date
date= date_price.tolist()

closing_price=df.Close
close = closing_price.tolist()


p = figure(x_range=date, title=" Counts",
           toolbar_location=None, tools="")

p.vbar(x=date, top=close, width=0.1)

p.xgrid.grid_line_color = None
p.y_range.start = 0

show(p)

