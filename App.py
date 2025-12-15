import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

st.header("Introduzindo os elementos do Streamlit")

menu = option_menu(
    menu_title="Menu",
    options=["Início", "Gráficos Estatísticos", "Gráficos Dinâmicos", "Widgets", "Formulário"],
    icons=["house-fill", "bar-chart-fill", "bar-chart-line-fill", "toggles", "ui-checks"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)

def carregar_dados(dados):
    try:
        df = pd.read_excel(dados)
        return df
    except FileNotFoundError:
        return pd.DataFrame()


with st.sidebar:
    st.success("**UPLOAD DE DADOS**")
    dados = st.file_uploader(
        "Carregue...",
        type=["xlsx", "xls"]
    )

if dados:
    df = carregar_dados(dados)
    st.table(df)
else:
    st.info("Carregue um ficheiro Excel para começar")

