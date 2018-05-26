import dash
from dash.dependencies import Input, Output, State, Event
import dash_core_components as dcc
import dash_html_components as html
# import dash_table_experiments as dt
import plotly
from plotly import graph_objs as go
from plotly.graph_objs import *
from flask import Flask
import pandas as pd
import numpy as np
import os
import copy

MAP_BOX_ACCESS_KEY = 'pk.eyJ1IjoiZ2FicmllbG1sZyIsImEiOiJjamZibmFibWgzMHFrMnhwNGZnN2w0ZzVmIn0.E32pbcfKBFON9p3D532Uaw'
map_data = pd.read_csv(os.getcwd() + '/datasets/mapDemoCbk.csv', sep=';', encoding='latin_1')
# Estou aqui!!
map_data['Legend'] = map(lambda x: x['Local'] + ' - ', map_data)

layout_tmp = dict(
    autosize=True,
    height=800,
    font=dict(color="#191A1A"),
    titlefont=dict(color="#191A1A", size='14'),
    margin=dict(
        l=35,
        r=35,
        b=35,
        t=45
    ),
    hovermode="closest",
    plot_bgcolor='#fffcfc',
    paper_bgcolor='#fffcfc',
    legend=dict(font=dict(size=10), orientation='h'),
    title='Mapa de Fraude',
    mapbox=dict(
        accesstoken=MAP_BOX_ACCESS_KEY,
        style="light",
        center=dict(
            lon=-48.0774443,
            lat=-15.7215857
        ),
        zoom=4,
    )
)


def gen_map(map_data):
    # groupby returns a dictionary mapping the values of the first field
    # 'classification' onto a list of record dictionaries with that
    # classification value.
    return {
        "data": [
            {
                "type": "scattermapbox",
                "lat": list(map_data['Latitude']),
                "lon": list(map_data['Longitude']),
                "text": map_data['Local'],
                "mode": "markers",
                "name": list(map_data['Local']),
                "marker": {
                    "size": map_data['Qtde']/14,
                    "opacity": 0.7
                }
            }
        ],
        "layout": layout_tmp
    }


layout = html.Div(
    [
        html.Div(
            [
                dcc.Graph(id='map-graph',
                          animate=True,
                          style={'margin-top': '20'},
                          figure=gen_map(map_data))
            ], className="six columns"
        )])
