import pandas as pd
from prophet import Prophet

# The incoming data from whatever source
data = 'https://raw.githubusercontent.com/facebook/prophet/main/examples/example_wp_log_peyton_manning.csv'

# input will be ds and y
# ds is date time stamp - YYYY-MM-DD HH:MM:SS
# y is the measurement to forecast - temp


df = pd.read_csv(data)
df.head()

m = Prophet()
m.fit(df)

future = m.make_future_dataframe(periods=10)
future.tail()

forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

