
import yfinance as yf
import streamlit as st

st.write("""
# Demo stock price

Stock closing price and volume of Google.
""")

ts = 'GOOGL'
td = yf.Ticker(ts)
tr = td.history(period='1d',start='2015-01-01',end='2020-12-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits
st.line_chart(tr.Close)
st.line_chart(tr.Volume)

