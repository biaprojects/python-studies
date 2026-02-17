# Vamos entender de fato!

## O que acontece com o read_excel?
Primeiro, vamos pensar em leitura de arquivo...  

Antes do `read_excel`, vamos entender.  
O que é um `DataFrame`?  

Uma tabela (tipo Excel / SQL), com linhas, colunas e um índice.  

Então, quando fazemos um `read_excel`, recebemos um `DataFrame`, algo semelhante a isso: 
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

Agora, vamos “olhar dentro” desse DataFrame  
->  `type(df)`

Resultado:  
->  `pandas.core.frame.DataFrame`

Agora:  
-> `df.columns`  -> pegar nome das colunas
Resultado:  
-> `Index(['nome', 'idade', 'cidade'], dtype='object')`

E:  
->  `df.index`  -> identificaação das linhas
Resultado:  
-> `RangeIndex(start=0, stop=3, step=1)`  -> traduzindo: começa em 0, vai até 2 de um em um


Ou seja... Quando você faz:  
`df = pd.read_excel("arquivo.xlsx")`

O que acontece é:
- Pandas lê o Excel
- Cria um DataFrame
- Define colunas
- Cria índice
- Infere tipos
- Tudo igual ao pd.DataFrame(dados) que fizemos agora.
