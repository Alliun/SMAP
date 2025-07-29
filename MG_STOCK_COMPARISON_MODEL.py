# Importing the Libraries-
import streamlit as st
from prophet import Prophet
from prophet.plot import plot_plotly
from datetime import date
import yfinance as yf
from plotly import graph_objs as go

START = "2021-01-01"
TODAY = date.today().strftime("%Y-%m-%d")
# App Title
st.title('Machine Guys Stock Comparison Model')
col1, col2 = st.columns(2, gap='Large')

# Unique key for the first text input in col1
stocks1 = col1.text_input("Enter stock ticker:", "ENTER STOCK", key="stock_input1")
n_years1 = col1.slider('Years of prediction:', 1, 4)
period1 = n_years1 * 365


def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

data_load_state = col1.text('Loading data...')
data1 = load_data(stocks1)
data_load_state.text('Loading data... done!')
col1.subheader('Raw data')
col1.write(data1.tail())

def plot_raw_data1():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data1['Date'], y=data1['Open'], name="stock_open"))
    fig.add_trace(go.Scatter(x=data1['Date'], y=data1['Close'], name="stock_close"))
    fig.update_layout(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True, width=500)
    col1.plotly_chart(fig)

with col1.container():
    plot_raw_data1()

def predict1():
    df_train = data1[['Date', 'Close']]
    df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

    m = Prophet()
    m.fit(df_train)
    future = m.make_future_dataframe(periods=period1)
    forecast = m.predict(future)

    col1.subheader('Forecast data')
    col1.write(forecast.tail())

    col1.write(f'Forecast plot for {n_years1} years')
    fig1 = plot_plotly(m, forecast)
    fig1.update_traces(marker=dict(color='red'))
    col1.plotly_chart(fig1, use_container_width=True)  # Adjusted to use_container_width

    col1.write("Forecast components for stock 1")
    fig2 = m.plot_components(forecast)
    col1.write(fig2)

col1.write(predict1())

# Unique key for the second text input in col2
stocks2 = col2.text_input("Enter stock ticker:", "ENTER STOCK", key="stock_input2")
n_years2 = col2.slider('Years of prediction for comparing:', 1, 4)
period2 = n_years2 * 365


def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

data_load_state = col2.text('Loading data...')
data2 = load_data(stocks2)
data_load_state.text('Loading data... done!')
col2.subheader('Raw data')
col2.write(data2.tail())

def plot_raw_data2():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data2['Date'], y=data2['Open'], name="stock_open"))
    fig.add_trace(go.Scatter(x=data2['Date'], y=data2['Close'], name="stock_close"))
    fig.update_layout(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True, width=500)
    col2.plotly_chart(fig)

with col2.container():
    plot_raw_data2()

def predict2():
    df_train = data2[['Date', 'Close']]
    df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

    m = Prophet()
    m.fit(df_train)
    future = m.make_future_dataframe(periods=period2)
    forecast = m.predict(future)
    col2.subheader('Forecast data')
    col2.write(forecast.tail())

    col2.write(f'Forecast plot for {n_years2} years')
    fig1 = plot_plotly(m, forecast)
    fig1.update_traces(marker=dict(color='red'))
    col2.plotly_chart(fig1, use_container_width=True)  # Adjusted to use_container_width

    col2.write("Forecast components for stock 2")
    fig2 = m.plot_components(forecast)
    col2.write(fig2)

col2.write(predict2())
