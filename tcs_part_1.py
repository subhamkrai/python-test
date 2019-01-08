#PART_1


from datetime import date
from nsepy import get_history
import pandas as pd
import matplotlib.pyplot as plt



tcs = get_history(symbol='TCS',start=date(2015,1,1),end=date(2016,12,31))

tcs.to_csv('tcs.csv')

df = pd.read_csv('tcs.csv')
closing_price=df.Close

df = pd.read_csv('tcs.csv')
volume_val=df.Volume


weekly_resampled_data = df.Close.resample('W').mean() 


#PART_1_1

# assumption 1 week = 5 working days  

print("Printing part 1")

print("Printing moving average of 4 weeks")
moving_avg_4Weeks=closing_price.rolling(window=20).mean()
print(moving_avg_4Weeks)
print() 


print("Printing moving average of 16 weeks")
moving_avg_16Weeks=closing_price.rolling(window=80).mean()
print(moving_avg_16Weeks)
print()


print("Printing moving average of 52 weeks")
moving_avg_52Weeks=closing_price.rolling(window=260).mean()
print(moving_avg_52Weeks)
print()

# Part_1_2


print("Printing data of window 10 and window 75 ")


temp=volume_val.index.values.tolist()

print("showing via graph")
weekly_resampled_data.rolling(window=10).mean().plot()
weekly_resampled_data.rolling(window=75).mean().plot()


print("printing data")
window_10=weekly_resampled_data.rolling(window=10).mean()
windows_75weekly_resampled_data.rolling(window=75).mean()

print(window_10)
print()
print(window_75)
print()

#PART_1_3


#Volume_shock

print("Printing volume_shock")
print()
volume_shock =[]
for i in range(1,len(temp)):
    if(volume_val[i]>(volume_val[i-1]+(.1*volume_val[i-1]))):
        volume_shock.append(1)
    else:
        volume_shock.append(0)
print(volume_shock)
print()


#Price_shock and same for Pricing black swan and Pricing shock with Volume shock

print()
print("Printing Price_shock and same for Pricing black swan and Pricing shock with Volume shock")
temp=closing_price.index.tolist()
price_shock=[]
for i in range(0,len(temp)-1):
    if(closing_price[i+1]-closing_price[i]>(.02*(closing_price[i+1]-closing_price[i]))):
        price_shock.append(1)
    else:
        price_shock.append(0)


print(price_shock)
