import streamlit as st
import predictor
import pandas as pd
import altair as alt
import numpy as np
import calendar
from datetime import date, timedelta

st.header("Purchase Flight Tickets at the Right Time and Save Money")
st.text("Nonstop Flights from Raleigh (RDU) Airport")
#destination = st.text_input("Destination")
#st.sidebar.title("Enter Date and Destination of the Flight")
#destination = st.sidebar.text_input("Destination")
destination = st.selectbox(
    'Destination',
    ('Atlanta','Austin','Boston','Charlotte','Chicago','Cincinati','Dallas','Denver',
               'Fort Lauderdale','Detroit','Houston','Las Vegas','Los Angeles','Miami','Minneapolis',
               'Nashville','New York','Orlando',
               'Philadelphia','Phoenix', 'Pittsburgh','San Francisco','Seattle','Tampa','Washington'))
flight_date = st.date_input("Flight Date")
win_start_date,win_end_date, min_price,int_prices = predictor.predict_best_time(destination,flight_date)
int_prices = [int(i) for i in int_prices]
int_prices[0]=int((int_prices[0]+int_prices[1])/2)
int_prices.reverse()
Date = []
for i in range(0,60,4):
    date = flight_date - timedelta(i)
    Date.append(date.strftime("%b %d"))
Date.reverse()
    #############
d = ({'Date':Date, 'Ave Price': int_prices, 'Interval':['4 days','4 days','4 days','4 days',
                                                        '4 days','4 days','4 days','4 days','4 days','4 days','4 days','4 days','4 days','4 days','4 days']})
my_df = pd.DataFrame(d)
c = predictor.plot_bar(my_df)
c2 = predictor.plot_line(my_df)
################
if st.button("SUBMIT"):
    st.subheader("The cheapest time to book is likely :green[between "+ win_end_date.strftime("%b %d") +" and  " + win_start_date.strftime("%b %d")+".] "+"Minimum estimated price is around :green[$"+ str(min_price)+".]")
    st.altair_chart(c, use_container_width=True)
    #st.altair_chart(c2, use_container_width=True)
    
    