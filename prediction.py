
from prophet import Prophet
import wrapper

def predict():
# The incoming data from whatever source
    data = wrapper.api_call()
    data.rename(columns={0: 'ds', 1: 'y'}, inplace=True)
    # input will be ds and y
    # ds is date time stamp - YYYY-MM-DD HH:MM:SS
    # y is the measurement to forecast - temp

    m = Prophet()
    m.fit(data)

    future = m.make_future_dataframe(periods=1)
    future.tail()

    forecast = m.predict(future)
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
    final = forecast.yhat.tail(1).values[0]
    temp = (final - 273.15) * (9.0 / 5) + 32

    return temp
