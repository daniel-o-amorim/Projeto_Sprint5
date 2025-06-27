import pandas as pd
import plotly.express as px
import streamlit as st

# Carregamento e limpeza:
df_vehicles = pd.read_csv('vehicles_us.csv')
df_vehicles['odometer_km'] = df_vehicles['odometer'] * 1.60934
df_vehicles = df_vehicles.dropna()
df_vehicles['model_year'] = df_vehicles['model_year'].astype(int)

# Configuração da página:
st.set_page_config(
    page_title="Relatório de Veículos",
    layout="centered",
    initial_sidebar_state="auto"
)

# Estilo corrigido:
st.markdown("""
<style>
.Body {
    background-color: #f5f5f5;
    color: #111;
    font-family: 'Segoe UI', sans-serif;
}
.main {
    background-color: white;
    border-radius: 10px;
    padding: 1rem;
    font-size: 1rem;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
</style>
""", unsafe_allow_html=True)

st.title("Relatório de Veículos nos EUA")

# FILTROS na sidebar:
st.sidebar.header("Filtros")

modelo = st.sidebar.multiselect(
    "Modelo do veículo:",
    options=sorted(df_vehicles['model'].unique())
)

combustivel = st.sidebar.multiselect(
    "Tipo de combustível:",
    options=sorted(df_vehicles['fuel'].unique())
)

ano = st.sidebar.slider(
    "Ano do modelo:",
    int(df_vehicles['model_year'].min()),
    int(df_vehicles['model_year'].max()),
    (int(df_vehicles['model_year'].min()),
     int(df_vehicles['model_year'].max()))
)

# Aplicação dos filtros:
df_vehicles.copy()

if modelo:
    df_vehicles = df_vehicles[df_vehicles['model'].isin(modelo)]
if combustivel:
    df_vehicles = df_vehicles[df_vehicles['fuel'].isin(combustivel)]
if ano:
    df_vehicles = df_vehicles[
        (df_vehicles['model_year'] >= ano[0]) & 
        (df_vehicles['model_year'] <= ano[1])
    ]
st.markdown("Realize a filtragem e verifique os gráficos:")

# Histograma de preços:
if st.checkbox("Histograma de Preços"):
    st.subheader("Distribuição de Preços dos Veículos")
    fig_hist = px.histogram(df_vehicles, x='price', nbins=50,
                            title="Distribuição de Preços dos Veículos",
                            labels={'price': 'Preço (USD)'})
    st.plotly_chart(fig_hist)
    st.caption(
        "O gráfico exibe a distribuição de preços dos veículos no conjunto de dados filtrado.")

# Histograma de quilometragem:
if st.checkbox("Histograma de Quilometragem (KM)"):
    st.subheader('Histograma de Quilometragem')
    fig_odo = px.histogram(df_vehicles, x='odometer_km', nbins=50,
                           title='Distribuição de Quilometragem (KM)')
    st.plotly_chart(fig_odo)

# Gráficos de dispersão:
if st.checkbox("Exibir gráficos de dispersão"):
    st.subheader("Gráficos de Dispersão")
    opcao_disp = st.selectbox("Escolha a relação para visualizar:", [
        "Ano do Modelo vs Preço",
        "Quilômetro (KM) vs Preço",
        "Ano do Modelo vs Quilômetro (KM)",
        "Cilindros vs Preço",
        "Dias listados vs Preço"
    ])

    if opcao_disp == "Ano do Modelo vs Preço":
        fig_disp = px.scatter(df_vehicles, x='model_year', y='price',
                              title="Ano do Modelo vs Preço",
                              labels={'model_year': 'Ano do Modelo',
                                      'price': 'Preço (USD)'},
                              opacity=0.5)
        st.plotly_chart(fig_disp)
        st.caption(
            "O gráfico mostra se veículos mais novos tendem a ter preços mais altos.")
    elif opcao_disp == "Quilômetro (KM) vs Preço":
        fig = px.scatter(df_vehicles, x='odometer_km', y='price',
                         title='Quilômetro (KM) vs Preço',
                         labels={
                             'odometer_km': 'Quilômetro (KM)', 'price': 'Preço (USD)'},
                         opacity=0.5)
        st.plotly_chart(fig)
    elif opcao_disp == "Ano do Modelo vs Quilômetro (KM)":
        fig = px.scatter(df_vehicles, x='model_year', y='odometer_km',
                         title='Ano do Modelo vs Quilômetro (KM)',
                         labels={'model_year': 'Ano do Modelo',
                                 'odometer_km': 'Quilômetro (KM)'},
                         opacity=0.5)
        st.plotly_chart(fig)
    elif opcao_disp == "Cilindros vs Preço":
        fig = px.scatter(df_vehicles, x='cylinders', y='price',
                         title='Cilindros vs Preço',
                         labels={'cylinders': 'Número de Cilindros',
                                 'price': 'Preço (USD)'},
                         opacity=0.5)
        st.plotly_chart(fig)
    elif opcao_disp == "Dias listados vs Preço":
        fig = px.scatter(df_vehicles, x='days_listed', y='price',
                         title='Dias listados vs Preço',
                         labels={'days_listed': 'Dias listados',
                                 'price': 'Preço (USD)'},
                         opacity=0.5)
        st.plotly_chart(fig)

# Download dos dados filtrados:


@st.cache_data
def convert_df(df_vehicles):
    return df_vehicles.to_csv(index=False).encode('utf-8')


csv = convert_df(df_vehicles)

st.download_button(
    label="Baixar Dados Filtrados",
    data=csv,
    file_name='dados_veiculos_filtrados.csv',
    mime='text/csv'
)
