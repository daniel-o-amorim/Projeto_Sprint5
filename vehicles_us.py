import pandas as pd
import plotly.express as px
import streamlit as st

# Carregamento e Limpeza dos dados:
df_vehicles = pd.read_csv('vehicles_us.csv')
df_vehicles['odometer_km'] = df_vehicles['odometer'] * 1.60934

df_vehicles.dropna(subset=['price', 'model_year',
                   'odometer', 'fuel'], inplace=True)

# Config. da Página:
st.set_page_config(
    page_title="Relatório de Veículos",
    layout="centered",
    initial_sidebar_state="auto"
)
# Estilo da página:
st.markdown(
    """
    <style>
    .Body {
        background-color: #f5f5f5;
        color: #111;
        font-family: 'Seagoe UI' , sans-serif;
    }
    .main {
    background-color: white;
        border-radius: 10px;
        padding: ;
        color: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    </style>
    """, unsafe_allow_html=True
)

st.title("Relatório de Veículos nos EUA")

# Filtros adicionais
st.sidebar.header("Filtros")
modelos = st.sidebar.multiselect(
    "Modelo do veículo:", options=sorted(df_vehicles['model'].unique()))
combustivel = st.sidebar.multiselect(
    "Tipo de combustível:", options=sorted(df_vehicles['fuel'].unique()))
ano = st.sidebar.slider("Ano do modelo:", int(df_vehicles['model_year'].min()), int(
    df_vehicles['model_year'].max()), (2010, 2020))

# Aplicação dos filtros:
df_vehicles = df_vehicles.copy()
if modelos:
    df_vehicles = df_vehicles[df_vehicles['model'].isin(modelos)]
if combustivel:
    df_vehicles = df_vehicles[df_vehicles['fuel'].isin(combustivel)]
if ano:
    df_vehicles = df_vehicles[(df_vehicles['model_year'] >= ano[0]) & (
        df_vehicles['model_year'] <= ano[1])]

st.markdown("Análise visual com filtros aplicados:")

# Histograma de Preços:
if st.checkbox("Histograma de Preços"):
    st.subheader("Distribuição de Preços dos Veículos")
    fig_hist = px.histogram(df_vehicles, x='price', nbins=50,
                            title="Distribuição de Preços dos Veículos",
                            labels={'price': 'Preço (USD)'})
    st.plotly_chart(fig_hist)
    st.caption(
        "O gráfico exibe a distribuição de preços dos veículos no conjunto de dados filtrado.")

# Gráfico de Dispersão:
st.subheader("Gráficos de Dispersão")

if st.checkbox("Exibir gráficos de dispersão"):
    opcao_disp = st.selectbox("Escolha a relação para visualizar:", [
        "Ano do Modelo vs Preço",
        "Quilometro (KM) vs Preço",
        "Ano do Modelo vs Quilometro (KM)",
        "Cilindros vs Preço",
        "Dias listados vs Preço",
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
    elif opcao_disp == "Odômetro (KM) vs Preço":
        fig = px.scatter(df_vehicles, x='odometer_km', y='price',
                         title='Odômetro (KM) vs Preço',
                         labels={
                             'odometer_km': 'Odômetro (KM)', 'price': 'Preço (USD)'},
                         opacity=0.5)
        st.plotly_chart(fig)

    elif opcao_disp == "Ano do Modelo vs Odômetro (KM)":
        fig = px.scatter(df_vehicles, x='model_year', y='odometer_km',
                         title='Ano do Modelo vs Odômetro (KM)',
                         labels={'model_year': 'Ano do Modelo',
                                 'odometer_km': 'Odômetro (KM)'},
                         opacity=0.5)
        st.plotly_chart(fig)

# ======== FILTROS E ANÁLISES ADICIONAIS ========
st.subheader("Análises com Filtros")

# Filtros para Marcas, Combustível e Faixa de Anos
marca = st.selectbox("Escolha a marca:", df_vehicles['make'].unique())
combustivel = st.selectbox(
    "Escolha o tipo de combustível:", df_vehicles['fuel'].unique())
faixa_anos = st.slider("Escolha a faixa de anos:",
                       int(df_vehicles['model_year'].min()), int(
                           df_vehicles['model_year'].max()),
                       (int(df_vehicles['model_year'].min()), int(df_vehicles['model_year'].max())))

# Filtrar os dados com base nos filtros escolhidos
df_filtrado = df_vehicles[(df_vehicles['make'] == marca) & (df_vehicles['fuel'] == combustivel) &
                          (df_vehicles['model_year'] >= faixa_anos[0]) & (df_vehicles['model_year'] <= faixa_anos[1])]

# Mostrar uma tabela com os dados filtrados
st.write(
    f"Mostrando {len(df_filtrado)} veículos com as características escolhidas:")
st.dataframe(df_filtrado)

# ======== DOWNLOAD DOS DADOS FILTRADOS ========


@st.cache
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')


csv = convert_df(df_filtrado)

st.download_button(
    label="Baixar Dados Filtrados",
    data=csv,
    file_name='dados_veiculos_filtrados.csv',
    mime='text/csv'
)

# ======== HISTOGRAMA DE QUILOMETRAGEM ========
st.subheader('Histograma de Quilometragem')

# Exibir histograma de quilometragem
if st.checkbox('Mostrar histograma do odômetro em KM'):
    fig_odo = px.histogram(df_vehicles, x='odometer_km', nbins=50,
                           title='Distribuição de Quilometragem (KM)')
    st.plotly_chart(fig_odo)
