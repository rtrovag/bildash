# Kilde: https://dash.plotly.com/
# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
#pip install dash
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
app = Dash(__name__)
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv("cars.csv")
print(df.head())
fig1 = px.bar(df, x="Weight", y="CO2", color="Volume", barmode="group")
fig2= px.scatter(df, x="Weight", y="CO2", color="CO2")

app.layout = html.Div(children=[
    html.H1(children='Biler'),
    html.Div(children='''
        Oversikt over vekt, CO2 og motorvolum
    '''),
    dcc.Graph(
        id='example-graph',
        figure=fig1
    ),
     dcc.Graph(
        id='example-graph2',
        figure=fig2
    )
])
if __name__ == '__main__':
    app.run_server(debug=True)