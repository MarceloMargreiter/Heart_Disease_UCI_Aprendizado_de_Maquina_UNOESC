# -*- coding: utf-8 -*- 
from ucimlrepo import fetch_ucirepo 
 
# Importa os dados 
heart_disease = fetch_ucirepo(id=45) 
dados = heart_disease.data.features 
 
# Acrescentando a coluna 'doenca' 
dados['doenca'] = 1 * (heart_disease.data.targets > 0) 
 
# Separando os atributos preditores do atributo alvo (target) 
X = dados.drop(columns='doenca') 
y = dados['doenca'] 
 
# print('Atributos preditores:\n', X.head()) 
# print('\nTarget (alvo):\n', y.head())


# Separação dos dados entre treino e teste 
from sklearn.model_selection import train_test_split 
 
# 20% do dataset são separados para treino 
# Parâmetro stratify: Garante que os conjuntos de treinamento e teste tenham a mesma proporção  
# de classes (ou rótulos) que o conjunto de dados original 
# Isso é particularmente útil ao lidar com conjuntos de dados desbalanceados, onde algumas  
# classes são sub-representadas. 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y) 
 
# Biblioteca xgb 
import xgboost as xgb 
 
# XGBoost é um algoritmo de aprendizado de máquina que pertence à categoria de aprendizado  
# por conjunto (ensemble), especificamente à estrutura de reforço de gradiente  
# Ele utiliza árvores de decisão como aprendizes base e emprega técnicas de regularização  
# para aprimorar a generalização do modelo 
modelo = xgb.XGBClassifier(objective='binary:logistic') 
 
# Treina o modelo usando o subconjunto de treinamento 
modelo.fit(X_train, y_train) 
 
# Faz predições usando os dados de teste 
preds = modelo.predict(X_test) 
 
# Avaliação do modelo 
from sklearn.metrics import accuracy_score 
 
acuracia = accuracy_score(y_test, preds) 
print(f'A acurácia do modelo é de {acuracia:.2%}') 
 
# Biblioteca com várias funções úteis para processamento paralelo 
import joblib   
 
# Grava em disco o modelo treinado em um arquivo no formato 'pickle'
medianas = X.median ()                      # Calcula as medianas
joblib.dump(modelo, 'modelo_xgboost.pkl')   # Grava em disco o modelo treinado
joblib.dump(medianas, 'medianas.pkl')      # Grava em disco as medianas dos atributos calculadas