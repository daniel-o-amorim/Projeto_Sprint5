# Projeto_Sprint5
Este projeto faz parte do Bootcamp de Análise de Dados.
Objetivo: desenvolver aplicativo web interativo usando Streamlit.
Tema: Analise de Dados sobre veículos nos Estados Unidos. 

Visualização interativa de histogramas e gráficos de dispersão,
Opçoes de filtragens de colunas relevantes (price e odometer)
Layout responsivo e visual objetivo.
Conversão automática de valores do odometro de milhas para quilometros
Compativel com Render.com para deploy online.

--
Python
Pandas
Plotly Express
Streamlit

---
Projeto_Sprint5/
│
├── app.py # Arquivo principal da aplicação Streamlit
├── vehicles_us.csv # Base de dados usada no projeto
├── streamlit/
│ └── config.toml # Configuração para deploy no Render
├── venv_sprint5/ # Ambiente virtual (não incluído no repositório remoto)
└── README.md # Este arquivo

---

Como executar:

Clone o repositório:
https://github.com/dsamorimInsights/Projeto_Sprint5.git
Projeto_Sprint5

Se já tiver criado o ambiente:
.\venv_sprint5\Scripts\activate

Instale os pacotes necessários
pip install -r requirements.txt

execute:
streamlit run vehicles_us.py

Daniel Amorim
Bootcamp de Análise de Dados - TRIPLETEN
Licenciado em Publicidade, Marketing e Relações Públicas
Pós-Graduado em Branding (IPAM)








