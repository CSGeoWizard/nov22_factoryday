from dash import Dash, dcc, html, Input, Output, State, dash_table, ctx
import prediction


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div([
    html.Button("Get Weather Prediction", id="run-weather", style={"margin": "15px"}, n_clicks=0),
    html.Div(id="return-weather", children=[])
    ]
)


@app.callback(
    Output('return-weather', 'children'),
    Input('run-weather', 'n_clicks')
)
def weather(clicks):
    if "run-weather" == ctx.triggered_id:
        temp = prediction.predict()
        return ["According to Intel Support and Wes, Tomorrow's High Temperature will be: " + str(int(temp))]
                # html.Div([dash_table.DataTable(temp)])] # Weather data


if __name__ == '__main__':
    app.run_server(debug=True)