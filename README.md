# Heart_Disease_UCI_Aprendizado_de_Maquina_UNOESC
**Trabalho para disciplina de Aprendizado de Máquina - UNOESC**


## Tecnologias utilizadas
- Python 3.11+
- Pandas
- Plotly
- Numpy
- Seaborn
- Joblib
- Dash
- HTML
- CSS
- Scikit-learn
- XGBoost
- Git/Github
- Google Cloud
- Docker

## Como executar o projeto

1→ No Promt do VS Code, vá até o diretório dessignado ao projeto, crie e ative o ambiente virtual:
``` 
Criar →     python -m venv .venv        (Obs.: Caso já exista, não há necessidade de executar novamente)

# Windows
Ativar →    .venv\Scripts\activate

# Linux ou MacOS
Ativar →    source .venv/bin/activate
```

2→ Instale os pacotes necessários no ambiente virtual:

```bash
pip install -r requirements.txt
``` 

3→ Execute o arquivo abaixo para gerar o modelo de previsão e verifique a acurácia do modelo:
```bash
Arquivo = "treina_modelo.py"
```

4→ Execute o programa e clique no link gerado para visualizar localmente:
```bash
Programa = "main.py"
Link = "http://127.0.0.1:8050/"
```

## Problemas
- Alto índice de espera na triagem de pacientes com suspeitas de doenças cardíacas.
- Falta de entendimento das *features* dos exames no contexto geral.

## Requisitos do negócio
- Criar um Dashboard para ajudar a prever pacientes com chances de doenças cardíacas.
- Criar graficos para entender melhor os dados (*features*) sobre o estado de saúde de pessoas com doenças cardíacas.
- Disponibilizar o dasboard online para interação do cliente (*usuário*).