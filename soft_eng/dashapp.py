from dash import Dash, dcc, html, Input, Output, State, dash_table, ctx
import plotly.graph_objs as go
import pandas as pd
from datetime import datetime, date, timedelta
import json


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div([
    html.Button("Get Weather Prediction", id="run-weather", style={"margin": "15px"}, n_clicks=0),
    html.Div(id="return-weather")
    ]
)


@app.callback(
    Output('return-weather', 'children'),
    Input('run-weather', 'n_clicks')
)
def weather(clicks):
    if "run-weather" == ctx.triggered_id:
        return ["Tomorrow's High Temperature will be: "] # Weather data


if __name__ == '__main__':
    app.run_server(debug=True)