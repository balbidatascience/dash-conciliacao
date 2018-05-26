import plotly.plotly as py
import dash_html_components as html
import dash_core_components as dcc

data = {'type': 'sankey',
        'node': {'pad': 20, 'thickness': 15, 'line': dict(
            color="black",
            width=0.5
        ), 'label': ["Circo Voador", "Palacio das Artes", "Aprovado", "Reprovado", "Manual - Aprovado",
                     "Manual - Reprovado"], 'color': ["gray", "blue", "green", "red", "green", "red"]}, 'link': {
    'source': [0, 1, 0, 0, 0, 1, 1, 1],
    'target': [2, 3, 3, 4, 5, 4, 5, 2],
    'value': [120, 90, 40, 20, 7, 30, 15, 40]
}}

layout = {'title': "Análise dos Pedidos", 'font': {'size': 15}}

fig = dict(data=[data], layout=layout)

appPage = html.Div(
    [
        html.Div(className='col-8',
                 children=[
                     dcc.Graph(id='sankey-graph',
                               animate=True,
                               style={'margin-top': '20'},
                               figure=fig)
                 ]
                 )])
