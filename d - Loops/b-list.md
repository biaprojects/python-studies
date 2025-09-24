# Listas
Em python, para declarar uma lista, basta inserir colchetes ([]).  

```
lista = []
```

Essa é uma lista vazia.

Se formos declarar ela já com valores inseridos, faremos:  

```
lista = [item1, item2, item3]
```

Na linguagem python, as listas aceitam diversos valores, ou seja, podemos mesclar números, strings, tudo dentro da mesma lista.

Uma lista é organizada por posições, sendo a primeira 0.

## Acessando posição
```
carros = ["fit", "etios"]

print(carros[0])
```

O sistema imprimirá `fit`.

## Algumas funções
|                  ação                  |     comando      | 
| :------------------------------------: | ---------------- | 
|            acrescentar item            |   .append(item)  |
|     acrescentar item na posição x      | .insert(x, item) |
|           pegar último item            |      .pop()      |
|        pegar item da posição x         |     .pop(x)      |
| organizar em ordem númerica/alfabética |     .sort()      |
