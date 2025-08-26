# -*- coding: utf-8 -*- 
from ucimlrepo import fetch_ucirepo 
import plotly.express as px 
from dash import Dash, dcc, html 
 
# Importa os dados 
heart_disease = fetch_ucirepo(id=45) 
dados = heart_disease.data.features 
 
# Acrescentando a coluna 'doenca' 
dados['doenca'] = 1 * (heart_disease.data.targets > 0) 
 
# Análise exploratória 
#print(dados.head()) 
 
# Cria o histograma 
fig_hist = px.histogram(dados, x='age', nbins=30, title='Distribuição Etária (Plotly)', 
color='doenca') 
fig_hist.update_layout(xaxis_title='Idade', yaxis_title='Frequência') 
 
# Cria o boxplot 
fig_box = px.box(dados, x='doenca', y='age', title='Distribuição Etária por Doença', color='doenca') 
fig_box.update_layout(xaxis_title='Diagnóstico (0 = não | 1 = sim)', yaxis_title='Idade') 
 
# Cria as divs 
div_hist = html.Div([ 
    html.H2('Histograma de Idades'),             
    dcc.Graph(figure=fig_hist), 
]) 
 
div_box = html.Div([ 
    html.H2('Boxplot de Idades'),             
    dcc.Graph(figure=fig_box) 
]) 
 
# Instancia o aplicativo 
app = Dash(__name__) 
app.layout = html.Div([ 
        html.H1('Análise de Dados do UCI Repository Heart Disease'), 
        div_hist, 
        div_box 
    ]) 
 
app.run(debug=True) 