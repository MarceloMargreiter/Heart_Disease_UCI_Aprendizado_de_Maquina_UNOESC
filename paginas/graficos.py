# -*- coding: utf-8 -*- 
from ucimlrepo import fetch_ucirepo 
import plotly.express as px 
from dash import dcc, html 
import dash_bootstrap_components as dbc 
 
 
# Importa os dados 
heart_disease = fetch_ucirepo(id=45) 
dados = heart_disease.data.features 
 
# Acrescentando a coluna 'doenca' 
dados['doenca'] = 1 * (heart_disease.data.targets > 0) 
 
# Cria o histograma 
fig_hist = px.histogram(dados, x='age', nbins=30, title='Distribuição Etária', 
color='doenca') 
fig_hist.update_layout(xaxis_title='Idade (Doença: 0 = Não | 1 = Sim)', yaxis_title='Frequência') 
 
# Cria o boxplot 
fig_box = px.box(dados, x='doenca', y='age', title='Distribuição Etária por Doença', color='doenca') 
fig_box.update_layout(xaxis_title='Diagnóstico (Doença: 0 = Não | 1 = Sim)', yaxis_title='Idade') 

# Cria o histograma 2
fig_dist = px.histogram(
    dados, x='chol', color='doenca', 
    marginal='rug',  # Adiciona rug plot para densidade
    nbins=40, 
    opacity=0.7,
    histnorm='probability density',
    title='Distribuição por Colesterol'
)
fig_dist.update_layout(
    xaxis_title='Colesterol (Doença: 0 = Não | 1 = Sim)',
    yaxis_title='Densidade',
    bargap=0.05
)
div_dist = html.Div([dcc.Graph(figure=fig_dist)])

 
# Cria as divs 
div_hist = html.Div([ 
    dcc.Graph(figure=fig_hist) 
]) 
 
div_box = html.Div([ 
    dcc.Graph(figure=fig_box) 
]) 
 
layout = html.Div([
    html.H1('Análise de Dados do UCI Repository Heart Disease',
            className='text-center mb-4 custom-subtitle'),

    dbc.Container([
        dbc.Row([
            dbc.Col([div_hist], md=12)
        ])
    ]),

    html.Div(style={'marginTop': '30px'}),  # Espaço entre as linhas

    dbc.Container([
        dbc.Row([
            dbc.Col([div_box], md=6),
            dbc.Col([div_dist], md=6)
        ])
    ])
])