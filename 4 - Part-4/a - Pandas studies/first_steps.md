<div align="center">
  <img src="https://pandas.pydata.org/static/img/pandas.svg" width="300">
</div>  


Biblioteca Python usada para análise e manipulação de dados.  
Ela facilita trabalhar com dados em tabelas, como planilhas do Excel ou arquivos CSV.  

Vamos começar?

# Antes de tudo!
Não esqueça de fazer as importações necessárias!  
No terminal:  
`pip install pandas`
`pip install openpyxl`

## Agora, primeiro passo: vamos criar uma planilha!
Uma planilha pode ser interpretada como dados de chave: valor. Logo, para conseguir tratar os dados, precisaremos declarar um dict!

A estrutura será a seguinte:
- "nome_coluna": "valor_coluna"

E se precisarmos incluir vários dados como esse?  
Podemos fazer um array (lista) de dicts!

Exemplo:
```python
import pandas as pd

# Criando dicionário:
dados = {
    'chave': 'valor',
    'chave': 'valor
}

# Transformando o dicionário em um DataFrame:
df = pd.DataFrame(dados)

# Definindo o nome do arquivo que será criado:
arquivo_excel = "dados_carros.xlsx"
# podemos usar csv, também, por exemplo

# Salvando o dataFrame dentro do arquivo:
df.to_excel(arquivo_excel, index=false)
# index = false serve para não criar uma coluna apenas com a contagem de items
```

# 

## Mas, e se formos ler algum arquivo?
```python
df = pd.read_excel('nome-planilha.xlsx')
products = df.to_dict(orient='records')
```
