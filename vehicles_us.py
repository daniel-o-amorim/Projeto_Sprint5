import pandas as pd
import plotly.express as px
import streamlit as st

df_vehicles = pd.read_csv("vehicles_us.csv")

# Config da página:
st.set_page_config(
    page_title="Relatório de Veículos", layout="centered",
    initial_sidebar_state="auto"
)
st.header("Relatório de Veículos nos EUA")

# Estilização da Página:
st.markdown(
    """
    <style>
    .Body
        background-color: #f5f5f5;
        color: #111;
        font-family: 'Segoe UI', sans-serif;
    }
    .main {
        background-color: white;
        border-radius: 10px;
        padding: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
     }
     </style>
     """, unsafe_allow_html=True
)

# Cabeçalho:
st.title("Relatório de Veículos nos EUA")

# Converção de milhas para km:
df_vehicles['odometer_km'] = df_vehicles['odometer'] * 1.60934

# Caixa de Seleção para Histograma:
if st.checkbox('Histogramas de Preços:'):
    st.subheader('Histograma de Preços')
    fig_hist = px.histogram(df_vehicles, x='price', nbins=50,
                            title='Distribuição de Preços dos Veículos',
                            labels={'price': 'Preço (USD)'})
    st.plotly_chart(fig_hist)

    # Caixa de Seleção Grafico de Dispersão:
    if st.checkbox('Mostrar dispersão entre ano e preço:'):
        st.subheader('Dispersão entre Ano e Preço')
        fig_disp = px.scatter(df_vehicles, x='model_year', y='price',
                              title='Dispersão entre Ano do Modelo e Preço',
                              labels={'model_year': 'Ano do Modelo',
                                      'price': 'Preço (USD)'},
                              opacity=0,
                              )
        st.plotly_chart(fig_disp)
# Caixa de Seleção: Odometer:
if st.checkbox('Mostrar histograma do odômetro em KM'):
    fig_odo = px.histogram(df_vehicles, x='odometer_km', nbins=50,
                           title='Distribuição de Quilometragem (KM)')
    st.plotly_chart(fig_odo)
