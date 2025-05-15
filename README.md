# Projeto_Sprint5
# Relatório de Análise de Veículos nos EUA

Este projeto é um aplicativo web interativo construído com Streamlit, que realiza uma análise exploratória dos dados de veículos usados nos Estados Unidos. A aplicação permite visualizar histogramas, gráficos de dispersão e aplicar filtros nos dados de forma prática e intuitiva.

## Funcionalidades

- Filtragem por marca, tipo de combustível e faixa de anos
- Visualização de histogramas para preços e quilometragens
- Geração de gráficos de dispersão entre variáveis selecionáveis
- Exibição de tabela de dados filtrados
- Download dos dados filtrados em .csv

## Estrutura do Projeto
.
├── README.md
├── vehicles_us.py # Código principal do app Streamlit
├── vehicles_us.csv # Base de dados
├── requirement.txt # Bibliotecas necessárias
├── notebooks/
│ └── EDA.ipynb # Análise exploratória (Jupyter)
└── streamlit/
└── config.toml # Configuração para Render

## Aplicativo Online

Acesse o aplicativo em:  
https://projeto-sprint5-danielamorim.onrender.com 

Para implantar este projeto na Render:

1. Suba o repositório para o GitHub
2. Acesse o site da Render e crie um novo Web Service
3. Conecte o repositório ao serviço
4. Configure os comandos:

- Build Command:
pip install --upgrade pip && pip install -r requirement.txt
- Start Command:
streamlit run vehicles_us.py

## Requisitos Atendidos

- Cabeçalho com texto
- Pelo menos 1 histograma
- Pelo menos 1 gráfico de dispersão
- Pelo menos um botão ou caixa de seleção
- Aplicativo acessível via navegador
- Estrutura de arquivos exigida:
.
├── README.md
├── vehicles_us.py
├── vehicles_us.csv
├── requirement.txt
├── notebooks/
│ └── EDA.ipynb
└── streamlit/
└── config.toml

## Fonte dos Dados

O dataset `vehicles_us.csv` contém dados de veículos usados à venda nos Estados Unidos, incluindo preço, marca, tipo de combustível, quilometragem e ano de fabricação.

## Autor

Daniel Amorim
Bootcamp de Análise de Dados - TRIPLETEN
Licenciado em Publicidade, Marketing e Relações Públicas
Pós-Graduado em Branding (IPAM)









