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

## Mudando default do print
O `print` possui como padrão, quebra de linha no final do comando. Mas podemos mudar isso!  
Digamos que queiramos imprimir várias coisas, em `print` separados, mas sem quebra de linha, e sim com vírgula ",".  

```
print(imprima, end=',')
```
