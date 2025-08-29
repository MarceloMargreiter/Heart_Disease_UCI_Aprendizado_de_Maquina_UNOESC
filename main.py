# -*- coding: utf-8 -*- 
from dash import dcc, html 
from dash.dependencies import Input, Output 
import dash_bootstrap_components as dbc 
import paginas 
from app import app 
 
 
navegacao = dbc.NavbarSimple( 
    children=[ 
        dbc.NavItem(dbc.NavLink('Gráficos', href='/graficos')), 
        dbc.NavItem(dbc.NavLink('Formulário', href='/formulario')), 
    ], 
    brand='Dashboard - Unoesc', 
    brand_href='/', 
    color='primary', 
    dark=True 
) 
 
app.layout = html.Div([ 
    dcc.Location(id='url', refresh=False), 
    navegacao, 
    html.Div(id='conteudo') 
]) 
 
@app.callback( 
    Output('conteudo', 'children'), 
    [Input('url', 'pathname')] 
) 
def mostrar_pagina(pathname): 
    if pathname == '/formulario': 
        return paginas.formulario.layout 
    elif pathname == '/graficos': 
        return paginas.graficos.layout 
    else: 
        return html.Div([
            html.H2("🏠 Bem-vindo à Página Inicial do Dashboard de Doenças Cardíacas", 
                    className='text-center mb-4', 
                    style={'color': '#2c3e50'}),
            html.P("Preencha o Formulário* para uma previsão sobre o estado de saúde do paciente ou visualize os Gráficos* e descubra insights sobre saúde cardiovascular.",
                className='text-center', 
                style={'fontSize': '18px', 'color': '#34495e'})
        ]) 
                
app.run(debug=True) 
