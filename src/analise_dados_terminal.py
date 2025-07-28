import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import os

MESES = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho']
META_VENDA = 55000


def carregar_planilha(mes):
    caminho = Path(__file__).resolve().parent.parent / 'data' / f'{mes}.xlsx'
    if not caminho.exists():
        print(f"Arquivo {caminho} não encontrado.")
        return None
    try:
        return pd.read_excel(caminho)
    except Exception as e:
        print(f"Erro ao ler {caminho}: {e}")
        return None


def mostrar_geral():
    for mes in MESES:
        tabela = carregar_planilha(mes)
        if tabela is not None:
            print(f"\n{mes.upper()}:")
            print(tabela)


def mostrar_vendedores():
    for mes in MESES:
        tabela = carregar_planilha(mes)
        if tabela is not None:
            print(f"\n{mes.upper()} - VENDEDORES:")
            print(tabela['VENDEDOR'].unique())


def relatorio_meta():
    print("\nMetas alcançadas por vendedores:")
    print("Selecione o mês para visualizar o relatório:")
    for i, mes in enumerate(MESES, start=1):
        print(f"[{i}] {mes.title()}")
    try:
        escolha = int(input("Digite o número do mês: "))
        mes_escolhido = MESES[escolha - 1]
    except (ValueError, IndexError):
        print("Opção inválida.")
        return

    tabela = carregar_planilha(mes_escolhido)
    if tabela is not None:
        atingiram_meta = tabela[tabela['VALOR'] > META_VENDA]
        if not atingiram_meta.empty:
            atingiram_meta = atingiram_meta.sort_values(by='VALOR', ascending=False)
            for _, linha in atingiram_meta.iterrows():
                print(f"- {linha['VENDEDOR']} bateu a meta em {mes_escolhido} com R$ {linha['VALOR']:.2f}")
            atingiram_meta['MÊS'] = mes_escolhido
            plotar_grafico(atingiram_meta, mes_escolhido)
            salvar_relatorio(atingiram_meta)
        else:
            print(f"Nenhum vendedor bateu a meta em {mes_escolhido}.")


def plotar_grafico(dados, mes):
    # Ordenar dados
    dados_ordenados = dados[['VENDEDOR', 'VALOR']].sort_values('VALOR', ascending=False)

    # Definir cores manuais
    cores = []
    for valor in dados_ordenados['VALOR']:
        if valor > META_VENDA * 1.2:
            cores.append('green')  # Acima de 66k
        else:
            cores.append('yellow')  # Entre 55k e 66k

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(dados_ordenados['VENDEDOR'], dados_ordenados['VALOR'], color=cores)

    ax.set_title(f"Meta batida - {mes.title()}")
    ax.set_ylabel('Valor (R$)')
    plt.xticks(rotation=45, ha='right')

    # Adiciona valores sobre as barras
    for i, valor in enumerate(dados_ordenados['VALOR']):
        ax.text(i, valor + 500, f"R$ {valor:.0f}", ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    plt.show()


def salvar_relatorio(dados):
    nome_arquivo = 'relatorio_metas.xlsx'
    try:
        dados.to_excel(nome_arquivo, index=False)
        print(f"\nRelatório salvo com sucesso em: {os.path.abspath(nome_arquivo)}")
    except Exception as e:
        print(f"Erro ao salvar o relatório: {e}")


def menu():
    while True:
        print("""
[1] Relatório Geral
[2] Vendedores
[3] Meta Batida com Gráfico
[4] Sair
""")
        try:
            opcao = int(input("Escolha a opção: "))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        if opcao == 1:
            mostrar_geral()
        elif opcao == 2:
            mostrar_vendedores()
        elif opcao == 3:
            relatorio_meta()
        elif opcao == 4:
            print("\nEncerrando....")
            break
        else:
            print("Opção inválida, tente novamente.")
        print("__" * 30)


if __name__ == "__main__":
    menu()
    print("\nSessão encerrada. Até logo!")
