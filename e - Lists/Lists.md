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
