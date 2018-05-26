import dash
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = html.Div([
    dcc.Link('Home', href='/'),
    html.Br(),
    dcc.Link('Conciliação', href='/apps/MonitorConciliacao'),
    html.Br(),
    dcc.Link('Acompanhamento Aprovação de Pedidos"', href='/apps/analisevendasaprovadas'),
    html.Br(),
    dcc.Link('Mapa de Chargeback"', href='/apps/monitorchargeback')
])