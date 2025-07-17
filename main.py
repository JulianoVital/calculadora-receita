# salve como app.py
import numpy as np
from scipy.integrate import trapezoid
import streamlit as st

st.title("Calculadora de Receita Projetada")

valores = st.text_area("Digite as receitas diárias separadas por vírgula:")

if valores:
    try:
        receita = [float(valor.strip()) for valor in valores.split(",")]
        dias = np.arange(1, len(receita) + 1)

        receita_acumulada = trapezoid(receita, dias)
        media_integral = receita_acumulada / (dias[-1] - dias[0])
        receita_projetada_31 = media_integral * (31 - 1)

        st.success(f"📊 Receita acumulada (até hoje): R$ {receita_acumulada:,.2f}")
        st.info(f"📈 Média diária estimada: R$ {media_integral:,.2f}")
        st.warning(f"📅 Receita total projetada até 31 dias: R$ {receita_projetada_31:,.2f}")
    except:
        st.error("Erro: Verifique se todos os valores são números válidos.")
