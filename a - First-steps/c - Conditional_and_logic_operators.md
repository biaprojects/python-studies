# Condicional
Mas e aqueles momentos de decisão?  
Se tal coisa... ai sim tal coisa.  
Como fazemos isso em nossos programas?

```
if condicional:
    comando
```

Se for verdadeiro (true) o comando será executado. Se não, ele sairá do loop e seguirá o programa.  

Mas e esse espaço, tipo um parágrafo. O que é isso?

Tudo que estiver com essa _indentação_ será os comandos dentro das condições.

Um exemplo clássico:

```
idade = int(input("Quantos anos você tem? "))

if idade >= 18:
    print("Você é maior de idade")
```

Mas, perceba uma coisa...  
Se a condição não for verdadeira, ele não executará nada. Mas e se eu quisesse informar quando a pessoa é menor de idade?

```
idade = int(input("Quantos anos você tem? "))

if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")
```

Ok, vimos como fazer condicional quando há 2 opções... Mas e se eu tivesse outras? Como fazer?

Por exemplo:  
- Idade menor que 0 ou maior que 120 dizer que não está correto;  
- De 0 a 17 que é menor de idade;  
- De 18 a 59 que é maior de idade;
- De 60 a 119 que é idoso.  

Opção 1:  
Vários if/else

```
idade = int(input('Quantos anos você tem? '))

if idade < 0:
    print('idade incorreta')
else:
    if idade < 18:
        print('menor de idade')
    else:
        if idade < 60:
            print('maior de idade')
        else:
            if idade < 120:
                print('60+')
            else:
                print('idade incorreta')
```

Opção 2:   
elif

```
idade = int(input('Quantos anos você tem? '))

if idade < 0:
    print ('idade incorreta')
elif idade < 18:
    print ('menor de idade')
elif idade < 60:
    print('maior de idade')
elif idade < 120:
    print ('60+')
else:
    print('idade incorreta')
```

Maaass... Tente encontrar algo que podemos "encurtar" nesse código.  

Concorda comigo que a primeira e a última condição têm o mesmo comando?  

Podemos "juntá-las" através de operadores lógicos!

# Operadores lógicos

| Portugês | Python |
| :------: | :----: | 
|    E     |  and   |
|    OU    |   or   | 
|   NÃO    |  not   |

Então... podemos _refatorar_ nosso código:
```
idade = int(input('Quantos anos você tem? '))

if idade < 0 or idade >= 120:
    print ('idade incorreta')
elif idade < 18:
    print ('menor de idade')
elif idade < 60:
    print('maior de idade')
else:
    print ('60+')
```
