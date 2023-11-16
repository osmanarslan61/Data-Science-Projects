import pandas as pd
from datetime import date, timedelta
import csv
import glob
import os
import calendar
import altair as alt
d = ({'Date':[1,2,3,4,5,6,7,8,9,10], 'Ave Price':[60, 80, 30, 40,50,100,20,45,70,90], 'month':['Oct','Oct','Oct','Oct','Oct','Oct','Oct','Oct','Oct','Oct']})
#my_df = pd.DataFrame(d)
def plot_bar(my_df):
    c=(alt.Chart(my_df, title="Average Ticket Prices Based on Historical Price Trends").mark_rect().encode(
        alt.X("Date",type='nominal',sort=None).title("Purchase Date"),
        alt.Y("Interval",type='ordinal',axis=alt.Axis(labels=False)).title(None),
        alt.Color("Ave Price",scale=alt.Scale(scheme='redyellowgreen'),sort="descending").title(None),
       tooltip =['Date',alt.Tooltip('Ave Price')])
       .configure_axis(
        labelFontSize=20,
        titleFontSize=20)
      )
    return c 

def plot_line(my_df):
    c2=(alt.Chart(my_df).mark_line().encode(
    alt.X("Date"), alt.Y("Ave Price")
    )
      )
    return c2   

#df = pd.concat(map(pd.read_csv, glob.glob(os.path.join('', "./Data/flight_prices_Sep*.csv"))))
df = pd.read_csv("./Data/lookup_table4.csv")
win_size=7
def predict_best_time(destination,flight_date):
    int_prices=[]
    weekday = calendar.day_name[flight_date.weekday()]
    win_start_index = df.loc[((df.Destination == destination) & (df.Weekday == weekday[0:3])), 'Best Win Index'].item()
    min_price = df.loc[((df.Destination == destination) & (df.Weekday == weekday[0:3])), 'Min Price'].item()
    win_size = df.loc[((df.Destination == destination) & (df.Weekday == weekday[0:3])), 'Window Size'].item()
    df2 = df.loc[((df.Destination == destination) & (df.Weekday == weekday[0:3]))]
    for i in range(6,21):
        int_prices.append(df2[df2.columns[i]].item())
    from datetime import date, timedelta
    win_start_date = flight_date - timedelta(win_start_index)
    win_end_date = win_start_date - timedelta(win_size)
    return win_start_date,win_end_date, min_price,int_prices 


