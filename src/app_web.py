import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Configurações iniciais
st.set_page_config(page_title="Dashboard de Vendas", layout="centered")
meses = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho']
meta_venda = 55000

def carregar_planilha(mes):
    caminho = Path.cwd().parent / 'data' / f'{mes}.xlsx'
    if not caminho.exists():
        st.warning(f"Arquivo {caminho} não encontrado.")
        return None
    return pd.read_excel(caminho)

def plotar_grafico(dados, mes):
    # Ordena valores
    dados_ordenados = dados[['VENDEDOR', 'VALOR']].set_index('VENDEDOR').sort_values('VALOR', ascending=False)
    
    # Definir cores manuais
    cores = []
    for valor in dados_ordenados['VALOR']:
        if valor > meta_venda * 1.2:  # Acima de 66.000
            cores.append('green')
        else:  # Entre 55.000 e 66.000
            cores.append('yellow')

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(dados_ordenados.index, dados_ordenados['VALOR'], color=cores)

    ax.set_title(f"Meta batida - {mes.title()}")
    ax.set_ylabel("Valor (R$)")
    plt.xticks(rotation=45, ha='right')

    # Adiciona valores sobre as barras
    for i, valor in enumerate(dados_ordenados['VALOR']):
        ax.text(i, valor + 500, f"R$ {valor:.0f}", ha='center', va='bottom', fontsize=9)

    st.pyplot(fig)

# Interface Streamlit
st.title("📊 Dashboard de Vendas")
mes_escolhido = st.selectbox("Selecione o mês:", meses)

if st.button("Gerar Relatório"):
    tabela = carregar_planilha(mes_escolhido)
    if tabela is not None:
        st.subheader(f"Dados de {mes_escolhido.title()}")
        st.dataframe(tabela)

        # Filtra apenas quem bateu meta
        atingiram_meta = tabela[tabela['VALOR'] > meta_venda]
        if not atingiram_meta.empty:
            st.subheader("Vendedores que bateram a meta:")
            st.dataframe(atingiram_meta[['VENDEDOR', 'VALOR']])
            plotar_grafico(atingiram_meta, mes_escolhido)
        else:
            st.info("Nenhum vendedor bateu a meta neste mês.")
