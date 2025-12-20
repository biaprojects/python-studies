<div align="center">
  <img src="https://pandas.pydata.org/static/img/pandas.svg" width="200">
</div>  


Biblioteca Python usada para análise e manipulação de dados.  
Ela facilita trabalhar com dados em tabelas, como planilhas do Excel ou arquivos CSV.  

Vamos começar?

## Primeiro passo: vamos criar uma planilha!
Uma planilha pode ser interpretada como dados de chave: valor. Logo, para conseguir tratar os dados, precisaremos declarar um dict!

A estrutura será a seguinte:
- "nome_coluna": "valor_coluna"

E se precisarmos incluir vários dados como esse?  
Podemos fazer um array (lista) de dicts!

Exemplo:



import pandas as pd

# 1. Criar um dicionário com os dados
dados = {
    "Marca": ["Honda", "Dodge", "Audi", "Ford"],
    "Carros": ["Civic", "Challenger", "R8", "Maverick" ],
    "Ano": [2020, 2018, 2023, 1970]
}

# 2. Transformar o dicionário em um DataFrame
df = pd.DataFrame(dados)

# 3. Definir o nome do arquivo Excel que será criado
arquivo_excel = "dados_carros.xlsx"

# 4. Salvar o DataFrame dentro do arquivo Excel
df.to_excel(arquivo_excel, index=False)

print(f"Arquivo '{arquivo_excel}' criado com sucesso!")


# Mas, e se formos ler algum arquivo?
df = pd.read_excel('nome-planilha.xlsx')
products = df.to_dict(orient='records')