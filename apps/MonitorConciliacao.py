from pandas import read_csv
from pandas import to_datetime
import pandas as pd
import os
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

df = read_csv(os.getcwd() + '/datasets/DemoConciliacaoVendasIR2018.csv', sep=';', encoding='latin_1')
df['data_compra'] = to_datetime(df['data_compra']).map(lambda x: x.date())
df_hist = df
df_hist = df[['data_compra', 'Conciliado', 'VlrCompra']].groupby(['data_compra', 'Conciliado']).sum()
df_hist.reset_index(level=['data_compra', 'Conciliado'], inplace=True)

def generate_barSales(df):
    pv = pd.pivot_table(df, index=['data_compra'], columns=["Conciliado"], values=['VlrCompra'], aggfunc=sum,
                        fill_value=0)

    trace1 = go.Bar(x=pv.index, y=pv[('VlrCompra', 'Conciliada')], name='Conciliada', marker={'color': '#678CDF'})
    trace2 = go.Bar(x=pv.index, y=pv[('VlrCompra', 'Divergente')], name='Divergente', marker={'color': '#C34C83'})
    trace3 = go.Bar(x=pv.index, y=pv[('VlrCompra', 'Em aberto')], name='Em aberto', marker={'color': '#5F3352'})

    return dcc.Graph(
        id='graph-bar-sales',
        figure={
            'data': [trace1, trace2, trace3],
            'layout':
                go.Layout(
                    title='Status das Vendas',
                    titlefont={'size': 20},
                    barmode='stack',
                    legend={
                        'font': {'size': 14}
                    },
                    xaxis={
                        'rangeselector': {
                            'buttons': [
                                {
                                    'step': 'all',
                                    'label': '#reset'
                                },
                                {
                                    'step': 'month',
                                    'label': '#mês',
                                    'stepmode': 'backward',
                                    'count': '1'
                                },
                                {
                                    'step': 'day',
                                    'stepmode': 'backward',
                                    'count': '7',
                                    'label': '#semana'
                                }
                            ],
                            'font': {'family': '\"Open Sans\", verdana, arial, sans-serif',
                                     "size": '12',
                                     'color': '#444'
                                     }
                        }
                    })
        })

def generate_barPayments(df):
    pv = pd.pivot_table(df, index=['data_compra'], columns=["Situacao"], values=['VlrCompra'], aggfunc=sum,
                        fill_value=0)

    trace1 = go.Bar(x=pv.index, y=pv[('VlrCompra', 'Liquidada')], name='Liquidada', marker={'color': '#16AFA6'})
    trace2 = go.Bar(x=pv.index, y=pv[('VlrCompra', 'Acatada')], name='Acatada', marker={'color': '#EDD267'})
    trace3 = go.Bar(x=pv.index, y=pv[('VlrCompra', 'Em aberto')], name='Em aberto', marker={'color': '#5F3352'})

    return dcc.Graph(
        id='graph-bar-payments',
        figure={
            'data': [trace1, trace2, trace3],
            'layout':
                go.Layout(
                    title='Status dos Recebíveis',
                    titlefont={'size': 20},
                    barmode='stack',
                    legend={
                        'font': {'size': 14}
                    },
                    xaxis={
                        'rangeselector': {
                            'buttons': [
                                {
                                    'step': 'all',
                                    'label': '#reset'
                                },
                                {
                                    'step': 'month',
                                    'label': '#mês',
                                    'stepmode': 'backward',
                                    'count': '1'
                                },
                                {
                                    'step': 'day',
                                    'stepmode': 'backward',
                                    'count': '7',
                                    'label': '#semana'
                                }
                            ],
                            'font': {'family': '\"Open Sans\", verdana, arial, sans-serif',
                                     "size": '12',
                                     'color': '#444'
                                     }
                        }
                    })
        })


layout = html.Div(

    [html.Div(className='container-fluid',
              children=[
                  html.H1(
                      children='Monitor Conciliação de Vendas',
                      style={
                          'textAlign': 'center'
                      }
                  )#,
                  #html.Div(children='Última atualização: ' + datetime.strftime(datetime.now(), "%d/%m/%Y %H:%M:%S"))
                  ]),

     html.Div(className='row justify-content-start',
              children=[
                  html.Div(
                      className='col-2',
                      children=[
                          html.Div(
                              className='card mb-5 box-shadow text-center',
                              children=[
                                  html.Div(className='card-header', children=[html.H6('Índice de Conciliação')]),
                                  html.Div(className='card-body', children=[html.H4('37%')])
                              ]
                          ),
                          html.Div(
                              className='card mb-5 box-shadow text-center',
                              children=[
                                  html.Div(className='card-header', children=[html.H6('Recebido do mês')]),
                                  html.Div(className='card-body', children=[html.H4('R$ 790K')])
                              ]
                          ),
                          html.Div(
                              className='card mb-5 box-shadow text-center',
                              children=[
                                  html.Div(className='card-header', children=[html.H6('A receber do mês')]),
                                  html.Div(className='card-body', children=[html.H4('R$ 1.2M')])
                              ]
                          )
                      ],
                      style={'margin-top': '150px'}),
                  html.Div(
                      className='col-10',
                      children=[generate_barSales(df),generate_barPayments(df)])
              ],
              style={'margin-left': '10', 'margin-right': '10'})
     ]

)