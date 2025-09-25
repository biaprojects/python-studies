# Listas

Em python, temos os seguintes tipos de listas:

## Tipo array
Para declarar uma lista tipo array, basta inserir colchetes ([]).  

```
lista = []
```

Essa é uma lista vazia.

Se formos declarar ela já com valores inseridos, faremos:  

```
lista = [item1, item2, item3]
```

Elas aceitam diversos valores, ou seja, podemos mesclar números, strings, tudo dentro da mesma lista.

Uma lista é organizada por posições, sendo a primeira 0.

### Acessando posição
```
carros = ["fit", "etios"]

print(carros[0])
```

O sistema imprimirá `fit`.

### Algumas funções
|      comando      |                  ação                  |
| :---------------: | -------------------------------------- | 
|   .append(item)   |            acrescentar item            |
|  .remove("item")  |              remover item              |
| .insert(x, item)  |     acrescentar item na posição x      |
|      .pop()       |           pegar último item            |
|      .pop(x)      |        pegar item da posição x         |
|      .sort()      | organizar em ordem númerica/alfabética |



## Lista tipo chave:valor (dict - dicionário)
Sintaxe:

```
dict = {}
```

Esse é um dicionário vazio.  
Para adicionar coisas, podemos, por exemplo:  

```
pessoa['nome'] = 'Beatriz'
```

Para acrescentar mais coisas, repetimos o passo anterior...  

```
pessoa['idade'] = 18
```

Ou, podemos já declarar no inicio...
```
pessoa = {'nome': 'Beatriz', 'idade': 18, 'altura': 1.6}
```

### É comum usar:
|  Função   |       Ação        |      Aplicado no exemplo anterior      |
| :-------: | :---------------: | :------------------------------------: |
|  .keys()  | Mostra as chaves  | dict_keys(['nome', 'idade', 'altura']) |
| .values() | Mostra os valores |    dict_values(['Beatriz', 18, 1.6])   |
