# Importing the Libraries-
import streamlit as st
from prophet import Prophet
from prophet.plot import plot_plotly
import statsmodels as sm
from datetime import date
import yfinance as yf
from plotly import graph_objs as go

 

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")
#App Tittle
st.title('Machine Guys Stock Forecast Model')

ticker_input=st.text_input("ENTER STOCK TICKER TO PREDICT","STOCK TICKER")

n_years = st.slider('Years of prediction:', 1, 4)
period = n_years * 365
#Loading data from y finance
@st.cache_data

def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

#Text for letting you know
data_load_state = st.text('Loading data...')
data = load_data(ticker_input)
data_load_state.text('Loading data... done!')
#Showcasing as a table
st.subheader('Raw data')
st.write(data.tail())
#Plots for raw data
def plot_raw_data():
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
	fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
	fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
	st.plotly_chart(fig)
plot_raw_data()
#Forecasting

def predict():
    df_train = data[['Date','Close']]
    df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

    m = Prophet()
    m.fit(df_train)
    future = m.make_future_dataframe(periods=period)
    forecast = m.predict(future)

    # Show and plot forecast


    st.subheader('Forecast data')
    st.write(forecast.tail())

    st.write(f'Forecast plot for {n_years} years')
    fig1 = plot_plotly(m, forecast)
    fig1.update_traces(marker=dict(color='red'))
    st.plotly_chart(fig1)

    st.write("Forecast components")
    fig2 = m.plot_components(forecast)

    st.write(fig2)
result= st.button("PREDICT")
st.write(result)
if result:
    st.write(predict())
    
