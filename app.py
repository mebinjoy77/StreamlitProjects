import streamlit as st
import pandas as pd
from pandas_datareader import data

tickers = ['AAPL', 'MSFT', '^GSPC']

start_date = '2010-01-01'
end_date = '2023-01-05'

df = data.DataReader("NASDAQ100", "fred", start_date, end_date)
df.fillna(0,inplace=True)
st.write(""" # Demo App """)
st.line_chart(df)


