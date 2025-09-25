# Vamos fazer nosso primeiro programa em python!

```
print("Hello World!")
```


## Saída de dados do programa para o mundo
`print()`
Essa é a função que imprime coisas em nossa tela!  


## Entrada de dados 
_Do mundo ao programa_

```
frase = input()
```

Onde:
> `frase` -> nome da variável  
> `input` -> função de entrada de dados  

Também é possível inserir uma mensagem dentro do input.  
Isso melhora a experiência e clareza de nosso código.  

Por exemplo:  

```
name = input("What's your name?")
```


## Juntando as 2
É possível realizar programas como:

```
name = input("What's your name? ")

print(name)
```

_O que está acontecendo?_

Nosso programa está pedindo que o usuário digite o nome dele, armazenando essa informação numa variável (através do `input`) e imprimindo-a (através do `print`)  


## Mas... E se não for um texto, e sim um número, como faço?
O input, como default (padrão) pensa em string (texto). Se formos fazer com algo diferente disso, teremos as opções:  

float(input())  -> para valores decimais  
int(input())  -> para valores inteiros

Por exemplo:  

```
height = float(input("Type your height: "))
age = int(input("Type your age: "))
```

É importante fazer essa diferenciação pois, no caso citado anteriormente, talvez essa mudança não fosse tão perceptiva, já que provavlemente o comando executado com as variáveis `height` e `age` seriam `print()`.  
Mas, no exemplo a seguir, isso seria um caso grave...  

```
speed = int(input("How fast were you? "))
distance = float(input("How far have you been? ))

time = distance/speed

print("You took:")
print(tempo)
```

Se não fosse especificado int e float, o programa iria dar erro.

_CASO TENHA ALGUMA DÚVIDA:_  
A função `type()` retorna o tipo que a variável se encaixa.  


## E se eu quiser definir quantas "casas" irei utilizar?
Podemos pensar nisso sobre...   
- Números decimais    
    `%.nf`  
    Onde:  
    - n = quantidade de casas decimais que o número terá.  
- Para organizar algum print  
    Digamos que iremos imprimir uma lista como se fosse uma tabela, para deixar mais organizado, podemos imprimi-lá com a "quantidade" de espaços de cada item pré determinados.  
    `%n.0f`  
    Onde:  
    - n = quantidade de "casas" que irá utilizar  
    - 0 porque não há valores depois da vírgula

Lembrando que isso só funciona com números!


## Imprimindo mais de uma coisa
- `print(nome, sobrenome)` -> inclui espaço em branco automaticamente.  
- `print(nome + sobrenome)` -> "gruda" um no outro
- `print(f"{nome} {sobrenome}")` -> permite formatar exatamente do jeito que deseja, incluindo as variáveis entre chaves.  

Exemplo:  
```
print("Hello world!")

name = input("What's your name? ")
print("Hello, " + name)

age = int(input("How old are you? "))
print("You're", age, "years old")

height = float(input("What's your height? (m) "))
print(f"Ok, {name}. You are {age} years old and {height}m tall.")
```

### Ao separar utilizando vírgula (,) o padrão é incluir um espaço. Mas e se eu quiser mudar isso?
```
print(variavel1, variavel2, variavel3, sep="separador")
```
Onde:  
Separador = o que queremos utilizar como separador entre as variáveis.


## Mudando default do print
O `print` possui como padrão, quebra de linha no final do comando. Mas podemos mudar isso!    
Digamos que queiramos imprimir várias coisas, em `print` separados, mas sem quebra de linha, e sim com vírgula ",".    

```
print(imprima, end=',')
```


## Imprimindo com marcadores:
Ex:  
```
nome = 'Beatriz'
idade = 18

print("Meu nome é %s" % nome)
print("Meu nome é %s e tenho %d anos" % (nome, idade))
```

As opções de marcadores que temos são:

| Marcador | Quando usar |
| :------: | :---------: |
|    %s    |    string   |
|    %d    |   inteiro   |
|    %f    |   decimal   |
