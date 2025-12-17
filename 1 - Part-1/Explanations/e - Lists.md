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
|     len(lista)    |       informa o tamanho da lista       |
|   .append(item)   |            acrescentar item            |
|  .remove("item")  |              remover item              |
| .insert(x, item)  |     acrescentar item na posição x      |
|      .pop()       |           pegar último item            |
|      .pop(x)      |        pegar item da posição x         |
|      .sort()      | organizar em ordem númerica/alfabética |

#### LEMBRANDO!!!
len(x) também _funciona com strings_

### Slicing
E se quisermos "cortar" nossa lista?   
Ex:  
```
numeros = [3, 1, 4, 1, 5, 9, 2, 0]

print(numeros[1:4])  # de item 1 a item 4
print(numeros[:3])   # de item 0 a 3
print(numeros[3:])   # de 3 ao fim
print(numeros[::2])  # de 2 em 2 (a partir de 0)
print(numeros[::-1]) # de tras pra frente
print(numeros[::])   # ela mesma
print(numeros[:])    # ela mesma
print(numeros[1:8:2])
```

Ou seja...  
|           Função | Ação                                                              |
| ---------------: | :---------------------------------------------------------------- |
|     lista[x : y] | de posição x até y                                                |
|       lista[x :] | de posição x até o fim                                            |
|       lista[: y] | de posição 0 até y                                                |
|    lista [: : z] | de z em z (a partir de 0) <br> - como se fosse passo em for-range |
|    lista[: : -1] | de tras pra frente                                                |
|       lista[: :] | a própria lista                                                   |
|         lista[:] | a própria lista                                                   |
| lista[x : y : z] | de posição x até posição y de z em z <br> inicio, fim e passo     |


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

