Mas... E quando identificamos um padrão ou queremos que o programa repita algo. Como fazer?

# For loop
Essa função itera item a item.  
Temos as seguintes formas de usar for:

## for in
```
for item in algo:
    comando
```

Pode ser usado em strings, listas.  
Exemplo:

```
nome = "Beatriz"

for letra in nome:
    print letra
```

O programa irá iterar, ou seja, passar letra por letra e imprimirá cada uma.

## for in range(n)
```
for item i range(n):
    comando
```

n -> número de vezes que queremos repetir.  
Mas... um detalhe importante:  
**Ele inicia em 0**. Ou seja, se digitarmos 3, por exemplo, serão 4 execuções (0, 1, 2, 3).

Mas, é possível mudar isso...

## for in range(x, n)
```
for item in range(x, n):
    comando
```

Assim, definimos o primeiro e o último número.  
Ex: de 1 a 3  ->  `for i in range(1, 3):`  
Assim, serão 3 execuções (1, 2, 3).

Mas... E se eu quiser ir "pulando"?

## For in range(x, n, y)
```
for item in range(x, n, y):
    comando
```

Assim, definimos início, fim e passso.

## Resumindo...
O for é extremamente útil quando sabemos, previamente, a quantidade de vezes que vamos executar determinado comando.  

# while loop
```
while condicao:
    comando
```

Obs: As variáveis da condição precisam, obrigatoriamente, serem declaradas antes do while.

Por exemplo:  
Vamos juntando valores até que chegue a um determinado valor.  
```
valor = 20
soma = 0

while soma < valor:
    acrescimo = int(input())
    soma += acrescimo
```

O que está acontecendo?  
Enquanto a condição for verdadeira, o comando será executado.  
Quando for falsa, ele finalizará o loop.
