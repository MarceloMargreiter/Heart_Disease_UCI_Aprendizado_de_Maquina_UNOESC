# -*- coding: utf-8 -*- 
from dash import Dash, dcc, html 
from dash.dependencies import Input, Output, State 
import dash_bootstrap_components as dbc 
import joblib 
import pandas as pd 
import numpy as np 
from app import app
 
 
# Carrega o modelo de IA 
modelo = joblib.load('modelo_xgboost.pkl')
medianas = joblib.load('medianas.pkl')



layout = html.Div([])


formulario = dbc.Container([ 
     html.P("Preencha as informações abaixo e clique no botão 'Prever' para executar o modelo", 
            className='text-center mb-4 custom-subtitle'),
    dbc.Row([ 
        dbc.Col([ 
            dbc.CardGroup([ 
                dbc.Label('Idade', className='custom-label'), 
                dbc.Input(id='idade', type='number', 
                          placeholder='Digite a idade',
                          class_name='custom-input') 
            ], className='mb-3'), 
            dbc.CardGroup([ 
                dbc.Label('Sexo biológico'), 
                dbc.Select(id='sexo', options=[ 
                    {'label': 'Masculino', 'value': '1'}, 
                    {'label': 'Feminino', 'value': '0'} 
                ],  class_name='custom-select') 
            ], className='mb-3'), 
            dbc.CardGroup([ 
                dbc.Label('Tipo de dor no peito', className='custom-label'), 
                dbc.Select(id='cp', options=[ 
                    {'label': 'Angina típica', 'value': '1'}, 
                    {'label': 'Angina atípica', 'value': '2'}, 
                    {'label': 'Dor não cardíaca', 'value': '3'}, 
                    {'label': 'Assintomático', 'value': '4'} 
                ],  class_name='custom-select') 
            ], className='mb-3'), 
            dbc.CardGroup([ 
                dbc.Label('Pressão arterial em repouso', className='custom-label'), 
                dbc.Input(id='trestbps', type='number', 
                          placeholder='Digite a pressão arterial em repouso',
                          class_name='custom-input') 
            ], className='mb-3'), 
            dbc.CardGroup([ 
                dbc.Label('Colesterol sérico', className='custom-label'), 
                dbc.Input(id='chol', type='number', 
                          placeholder='Digite o colesterol sérico',
                          class_name='custom-input') 
            ], className='mb-3'), 
            dbc.CardGroup([ 
                dbc.Label('Glicemia em jejum', className='custom-label'), 
                dbc.Select(id='fbs', options=[ 
                    {'label': 'Menor que 120 mg/dl', 'value': '0'}, 
                    {'label': 'Maior que 120 mg/dl', 'value': '1'}, 
                ],  class_name='custom-select') 
            ], className='mb-3'), 
            dbc.CardGroup([ 
                dbc.Label('Eletrocardiografia em repouso', className='custom-label'), 
                dbc.Select(id='restecg', options=[ 
                    {'label': 'Normal', 'value': '0'}, 
                    {'label': 'Anormalidades de ST-T', 'value': '1'}, 
                    {'label': 'Hipertrofia ventricular esquerda', 'value': '2'}, 
                ],  class_name='custom-select') 
            ], className='mb-3'), 
        ]), 
        dbc.Col([ 
            dbc.CardGroup([ 
                dbc.Label('Frequência cardíaca máxima atingida', className='custom-label'), 
                dbc.Input(id='thalach', type='number', 
                          placeholder='Digite a frequência cardíaca máxima atingida',
                          class_name='custom-input') 
            ], className='mb-3'), 
            dbc.CardGroup([ 
                dbc.Label('Angina induzida por exercício', className='custom-label'), 
                dbc.Select(id='exang', options=[ 
                    {'label': 'Não', 'value': '0'}, 
                    {'label': 'Sim', 'value': '1'}, 
                ],  class_name='custom-select') 
            ], className='mb-3'), 
            dbc.CardGroup([ 
                dbc.Label('Depressão do segmento ST induzida por exercício', className='custom-label'), 
                dbc.Input(id='oldpeak', type='number', 
                          placeholder='Depressão do segmento ST induzida por exercício',
                          class_name='custom-input') 
            ], className='mb-3'), 
            dbc.CardGroup([ 
                dbc.Label('Depressão do segmento ST', className='custom-label'), 
                dbc.Select(id='slope', options=[ 
                    {'label': 'Ascendente', 'value': '1'}, 
                    {'label': 'Plana', 'value': '2'}, 
                    {'label': 'Descendente', 'value': '3'}, 
                ],  class_name='custom-select') 
            ], className='mb-3'), 
            dbc.CardGroup([ 
                dbc.Label('Número de vasos principais coloridos por fluoroscopia', className='custom-label'), 
                dbc.Select(id='ca', options=[ 
                    {'label': '0', 'value': '0'}, 
                    {'label': '1', 'value': '1'}, 
                    {'label': '2', 'value': '2'}, 
                    {'label': '3', 'value': '3'}, 
                ],  class_name='custom-select')
            ], className='mb-3'), 
            dbc.CardGroup([ 
                dbc.Label('Cintilografia do miocárdio', className='custom-label'), 
                dbc.Select(id='thal', options=[ 
                    {'label': 'Normal', 'value': '3'}, 
                    {'label': 'Defeito fixo', 'value': '6'}, 
                    {'label': 'Defeito reversível', 'value': '7'}, 
                ],  class_name='custom-select') 
            ], className='mb-3'), 
            dbc.Button('Prever', id='botao-prever', color='success', n_clicks=0, 
                       className='mb-3 mt-3') 
        ]) 
    ]) 
], fluid=True) 
 
app.layout = html.Div([ 
    html.H1('Previsão de doença cardíaca', className='text-center mt-4 custom-title'), 
    formulario ,
     html.Div(id='previsao') 
]) 
 
 
@app.callback( 
    Output('previsao', 'children'), 
    [Input('botao-prever', 'n_clicks')],  # Chama a função sempre que for clicado no botão 'Prever' 
    [State('idade', 'value'), 
     State('sexo', 'value'), 
     State('cp', 'value'), 
     State('trestbps', 'value'), 
     State('chol', 'value'), 
     State('fbs', 'value'), 
     State('restecg', 'value'), 
     State('thalach', 'value'), 
     State('exang', 'value'), 
     State('oldpeak', 'value'), 
     State('slope', 'value'), 
     State('ca', 'value'), 
     State('thal', 'value')] 
) 
def prever_doenca(n_clicks, idade, sexo, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, 
slope, ca, thal): 
    if n_clicks == 0: 
        return '' 
     
    # Cria um DataFrame e já preenche seus dados com os valores do formulário 
    entradas_usuario = pd.DataFrame( 
        data = [[idade, sexo, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, 
thal]], 
        columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 
'oldpeak', 'slope', 'ca', 'thal'] 
    ) 

    # Preenche valores em branco com as medianas 
    entradas_usuario.fillna(medianas, inplace=True) 
 
    # oldpeak é float 
    entradas_usuario['oldpeak'] = entradas_usuario['oldpeak'].astype(np.float64) 
     
    # Converte números em formato string para int (exceto a coluna oldpeak tratada acima) 
    for col in entradas_usuario.columns: 
        if col != 'oldpeak': 
            entradas_usuario[col] = entradas_usuario[col].astype(int) 
 
    previsao = modelo.predict(entradas_usuario)[0] 
    if previsao == 1: 
        mensagem = 'Você tem doença cardíaca!' 
        cor_alerta = 'danger' 
    else: 
        mensagem = 'Você não tem doença cardíaca!' 
        cor_alerta = 'secondary' 
         
    alerta = dbc.Alert(mensagem, color=cor_alerta, className='d-flex justify-content-center mb-5')     
    return alerta 
 
 
 