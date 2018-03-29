import dash
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = html.Div([
    dcc.Link('Navigate to "/"', href='/'),
    html.Br(),
    dcc.Link('Navigate to Monitor da Conciliação', href='/apps/MonitorConciliacao'),
    html.Br(),
    dcc.Link('Acompanhamento Aprovação de Pedidos"', href='/apps/analisevendasaprovadas'),
    html.Br(),
    dcc.Link('Navigate to "/apps/app2"', href='/apps/app1')
])