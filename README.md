# 🎯 Projeto analise de dados (excel)

Este projeto implementa uma aplicação para análise de vendas utilizando Python, Pandas e Streamlit.
O sistema permite visualizar dados de vendas mensais a partir de planilhas Excel, destacando quais vendedores atingiram as metas estabelecidas, além de fornecer gráficos coloridos para facilitar a análise.

A aplicação conta também com uma versão para execução em terminal, sem interface web.


---

## 📌 **Funcionalidades**
- Leitura automática de planilhas Excel na pasta data/
- Identificação de vendedores que bateram a meta definida
- Visualização de relatórios no terminal ou interface web
- Estrutura simples e organizada, pronta para evoluir para banco de dados futuramente

---

## 🗂️ **Estrutura do Projeto**

analise-dados/  
│   
├── data/                       # Planilhas Excel com dados de vendas  
│   ├── janeiro.xlsx    
│   ├── fevereiro.xlsx  
│   └── ... 
│   
├── src/                          # Código-fonte  
│   ├── analise_terminal.py     # Versão para execução no terminal  
│   └── app.py                  # Versão web (Streamlit)    
│   
├── requirements.txt            # Lista de dependências do projeto  
└── README.md                   # Documentação  

---

## 🛑 **Pré-Requisitos**
- Python 3.9+
- visual studio code
- Navegador Web (para usar o Streamlit)
- Git
- Conta no GitHub

---

## 🎯 **Visão Geral**

Versão Terminal:
Permite navegar por menus para visualizar relatórios gerais e vendedores que bateram metas, exibindo gráficos diretamente no terminal.

Versão Web (Streamlit):
Interface simples e intuitiva com seleção de mês, visualização de dados e download do relatório filtrado em Excel.

Dados:
Planilhas mensais em Excel localizadas na pasta data/, podendo futuramente ser substituídas por banco de dados.

---

## 🖥️ **Execução do Projeto**

✅ **Usando o visual studio code**
1. Clone este repositório:
2. Certifique-se de ter o Python e dependências instaladas
    - No terminal execute: pip install -r requirements.txt
3. Execute o script: python analise_dados_terminal.py
4. Para o teste via Web (Streamlit)
5. Instale as dependências:
    - No terminal execute pip install -r requirements.txt
6. Execute o script: python -m streamlit run src/app_web.py
    - Acesse no navegador o endereço: http://localhost:8080 (irá aparecer no terminal)
---

## 📦 **Exemplo de interação**
✅ Visualização de dados de vendas mensais  
✅ Destaque visual para vendedores que superaram metas  
✅ Comparação de desempenho entre vendedores    

## 💡 **Possíveis Melhorias**
- Integração com banco de dados (MySQL ou PostgreSQL)
- Filtros avançados (por vendedor, período, etc.)
- Autenticação para uso seguro
- Deploy em nuvem (AWS)

---

## 👨‍💻 **Autor**
Desenvolvido por **Murilo**

✨ Transformar ideias em código. ✨

---

## 🤝 **Contribuições**
Sinta-se à vontade para abrir *issues* ou enviar *pull requests* para melhorias!
