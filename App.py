import streamlit as st
from streamlit_option_menu import option_menu
st.header("Introduzindo os elementos do Streamlit")
menu = option_menu(menu_title="Menu",
                   options =["Início", "Gráficos Estatísticos", "Gráficos Dinâmicos", "Widgets", "Formulário"],
                   icons = ["house-fill", "bar-chart-fill", "bar-chart-line-fill", "toggles", "ui-cheks"],
                   menu_icon = "cast",
                   default_index=0,
                   orientation="horizontal"
                  )
