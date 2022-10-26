import pandas as pd
import openpyxl
import matplotlib.pyplot as plt

opcao = 0
while opcao != 4:
    print('''\n

[1] Geral
[2] Vendedores
[3] Relatório meta batida com grafico
[4] Sair \n''')

    opcao = int(input("Escolha a opção: "))
    if opcao == 1:
        lista_meses = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho']
        for mes in lista_meses:
            tabela_vendas = pd.read_excel(f'{mes}.xlsx')
            print(mes, tabela_vendas)

    elif opcao == 2:
        lista_meses = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho']
        for mes in lista_meses:
            tabela_vendas = pd.read_excel(f'{mes}.xlsx')
            print(mes, tabela_vendas['VENDEDOR'])

    elif opcao == 3:
        print("Metas alcançadas por vendedores:\n ")
        lista_meses = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho']
        for mes in lista_meses:
            tabela_vendas = pd.read_excel(f'{mes}.xlsx')
            if (tabela_vendas[
                    'VALOR'] >= 55000).any():  # .ANY (ALGUM) - verificar se algum valor na coluna é maior que 55k, não quero pegar a coluna inteira
                VENDEDOR = tabela_vendas.loc[
                    tabela_vendas['VALOR'] > 55000, 'VENDEDOR'].values  # values, apresenta somente o valor
                VALOR = tabela_vendas.loc[tabela_vendas['VALOR'] > 55000, 'VALOR'].values
                print(
                    f'\n No mês de {mes} o(s) vendedor(es) {VENDEDOR}, bateram a meta com o valor total de R$ {VALOR}\n')
                grafico = tabela_vendas.loc[:, 'VENDEDOR':'VALOR']
                grafico.plot(kind='bar')
                plt.show()

    elif opcao == 4:
        print("\nEncerrando....")

    else:
        print("Opção invalida, por favor escolha uma opção.")
    print("__" * 30)
print("\nSessão encerrada, até logo!\n")