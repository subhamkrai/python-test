from datetime import date
import pandas as pd


df = pd.read_csv('infosys.csv')
volume_val=df.Volume

import numpy as np
from bokeh.plotting import figure, show, output_file




temp=volume_val.index.values.tolist()

volume_shock_1=[]

for i in range(1,len(temp)):
    if(volume_val[i]>(volume_val[i-1]+(.1*volume_val[i-1]))):
        volume_shock_1.append(i)



volume_shock_2=[]


df_1 = pd.read_csv('infosys.csv')
volume_val_1=df_1.Volume

#print(type(volume_val))
temp_1=volume_val_1.index.values.tolist()

volume_shock =[]
for i in range(1,len(temp_1)):
    if(volume_val_1[i]>(volume_val_1[i-1]+(.1*volume_val_1[i-1]))):
        volume_shock_2.append(i)



p = figure(width=1200, height=900, x_axis_type="datetime")
p.vbar(x=volume_shock_1, top=volume_shock_2, width=0.9,fill_color='Red')

show(p)
