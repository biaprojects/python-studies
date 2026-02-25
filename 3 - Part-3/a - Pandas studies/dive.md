# Vamos entender de fato!

# Primeiro, vamos pensar em leitura de arquivo...  

## O que acontece com o read_excel?
Antes de enteneder, de fato, o que esse comando faz... Vamos entender um pouco...  

O que é um `DataFrame`?  
-> Uma tabela (tipo Excel / SQL), com linhas, colunas e um índice.  

Quando fazemos um `read_excel`, recebemos um `DataFrame`, algo semelhante a isso: 

```python
import pandas as pd

dados = {
    "nome": ["Ana", "Bruno", "Carla"],
    "idade": [25, 30, 28],
    "cidade": ["SP", "RJ", "BH"]
}

df = pd.DataFrame(dados)
```

Porém, aqui declaramos um DataFrame manualmente.  

<br>

Agora, vamos “olhar dentro” desse DataFrame  
Comando:   
->  `type(df)`

Resultado:  
->  `pandas.core.frame.DataFrame`

<br> 

Agora...  
Comando:  
-> `df.columns`  -> pegar nome das colunas

Resultado:  
-> `Index(['nome', 'idade', 'cidade'], dtype='object')`

<br>

E...  
Comando:  
->  `df.index`  -> identificação das linhas

Resultado:  
-> `RangeIndex(start=0, stop=3, step=1)`  -> traduzindo: começa em 0, vai até 2 de um em um

<br>

Ou seja... Quando você faz:  
`df = pd.read_excel("arquivo.xlsx")`

O que acontece é:
- Pandas lê o Excel
- Cria um DataFrame
- Define colunas
- Cria índice
- Infere tipos
- Tudo igual ao pd.DataFrame(dados) que fizemos agora.

<br> 

# 

## E o to_dict?
`to_dict()` converte um DataFrame em um dicionário Python.  
Ou seja... visualmente:  

Isso:
```
   nome    idade cidade
0  Ana     25    SP
1  Bruno   30    RJ
2  Carla   28    BH
```

Usando `df.to_dict(orient="records")`  
Vira isso:  

```python
[
  {"nome": "Ana", "idade": 25, "cidade": "SP"},
  {"nome": "Bruno", "idade": 30, "cidade": "RJ"},
  {"nome": "Carla", "idade": 28, "cidade": "BH"}
]
```

Ou seja...
- Cada linha vira um dicionário
- Cada coluna vira uma chave
- O resultado é uma lista de dicionários

#

## orient
Primeiro... para que serve o `orient=""`?  
Esse comando define a estrutura e a direção dos dados ao converter um DataFrame para outros formatos.

Algumas das opções são:

### orient='records'
Lista de dicionários

```
[
  {
    "nome": "Ana", 
    "idade": 25,
    "cidade": "SP
  }
  {
    "nome": "Bruno", 
    "idade": 30,
    "cidade": "RJ
  }
  {
    "nome": "Carla", 
    "idade": 28,
    "cidade": "BH
  }
]
```

### orient='dict' -> (padrão)
`df.to_dict()`  
Dicionário de dicionários

Resultado:
```
{
  "nome": {0: "Ana", 1: "Bruno", 2: "Carla"},
  "idade": {0: 25, 1: 30, 2: 28},
  "cidade": {0: "SP", 1: "RJ", 2: "BH"}
}
```

Leitura:
- cada coluna é uma chave
- dentro, um dict index → valor

É útil para reconstruir um DataFrame depois.

### orient='list'
Dicionário de listas  
`df.to_dict(orient="list")

Resultado:

{
  "nome": ["Ana", "Bruno", "Carla"],
  "idade": [25, 30, 28],
  "cidade": ["SP", "RJ", "BH"]
}

### orient='index'
Dicionário de dicionários  
`df.to_dict(orient="index")`

Resultado:

{
  0: {"nome": "Ana", "idade": 25, "cidade": "SP"},
  1: {"nome": "Bruno", "idade": 30, "cidade": "RJ"},
  2: {"nome": "Carla", "idade": 28, "cidade": "BH"}
}

### Comparação rápida
| orient | Estrutura | Uso típico 
| ----- | ----- | ----- |
| records | lista de dict	| APIs / JSON |
| dict | dict de colunas | manter estrutura |
| list | dict de listas | dados simples |
| index |	dict por linha | índice significativo |


-> Regra de ouro:
Pandas primeiro. Conversão depois.

