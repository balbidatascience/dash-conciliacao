from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app
from apps import app1, MonitorConciliacao, index, MonitorChargeback, AnaliseVendasAprovadas


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return index.layout
    elif pathname == '/apps/monitorchargeback':
         return MonitorChargeback.layout
    elif str(pathname).lower() == '/apps/monitorconciliacao':
         return MonitorConciliacao.layout
    elif str(pathname).lower() == '/apps/analisevendasaprovadas':
         return AnaliseVendasAprovadas.appPage
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True, port=8051)
