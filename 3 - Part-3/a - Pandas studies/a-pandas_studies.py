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

teste