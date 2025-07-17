import numpy as np
from scipy.integrate import trapezoid
import streamlit as st
import datetime
import calendar

# 📆 Dados do mês atual
hoje = datetime.date.today()
ano_atual = hoje.year
mes_atual = hoje.month
dia_hoje = hoje.day
dias_do_mes = calendar.monthrange(ano_atual, mes_atual)[1]

st.title("📊 Calculadora de Receita Projetada")

st.markdown(f"Hoje é **{hoje.strftime('%d/%m/%Y')}** – estamos no dia **{dia_hoje}** de **{calendar.month_name[mes_atual]}**.")

valores = st.text_area("Digite as receitas diárias separadas por vírgula:")

if valores:
    try:
        receita = [float(valor.strip()) for valor in valores.split(",")]

        if len(receita) != dia_hoje:
            st.warning(f"⚠️ Você inseriu {len(receita)} valores, mas hoje é dia {dia_hoje}. Insira um valor para cada dia até hoje.")
        else:
            dias = np.arange(1, dia_hoje + 1)

            receita_acumulada = trapezoid(receita, dias)
            media_integral = receita_acumulada / (dias[-1] - dias[0])
            receita_projetada_mes = media_integral * (dias_do_mes - 1)
            receita_minima = receita_projetada_mes * 0.85

            st.success(f"✅ Receita acumulada ({dia_hoje} dias): R$ {receita_acumulada:,.2f}")
            st.info(f"📈 Média diária estimada: R$ {media_integral:,.2f}")
            st.warning(f"📅 Receita projetada para {calendar.month_name[mes_atual]}: R$ {receita_projetada_mes:,.2f}")
            st.error(f"🔻 Projeção com margem de erro de -15%: R$ {receita_minima:,.2f}")
    except:
        st.error("❌ Erro: Verifique se todos os valores são números válidos.")
