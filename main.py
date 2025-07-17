import numpy as np
from scipy.integrate import trapezoid
import streamlit as st
import datetime
import calendar

# Data atual
hoje = datetime.date.today()
ano_atual = hoje.year
mes_atual = hoje.month
dias_do_mes = calendar.monthrange(ano_atual, mes_atual)[1]

st.title("📊 Calculadora de Receita Projetada")

valores = st.text_area("Digite as receitas diárias separadas por vírgula:")

if valores:
    try:
        receita = [float(valor.strip()) for valor in valores.split(",")]
        dias = np.arange(1,


