# Objeto
Primeiro de tudo... O que é um objeto?  
'-> É uma entidade que formaliza o modo como compreendemos algo dentro de um sistema.  
'-> Um objeto sempre está associado ao seu estado e comportamento.

Exemplo:  
Objeto = Carro  
Atributos (propriedades/estados) => cor: preto | ano: 2020 | combustível: gasolina | velocidade: 0 km/h  
Métodos (comportamento) => acelerar() | frear() | acionar_farol()  


# Classe  
O que é uma clase?  
Conjunto de objetos semelhantes. Ou seja, um conjunto de artibutos e métodos comuns a objetos.  

Sintaxe:  
```  
class Nome: 
    def __init__(self, atributo1, atributo2):  
        self.atributo1 = atributo1  
        self.atributo2 = atributo2  
```

# Classe X Objeto
A principal diferença é que o objeto é uma entidade concreta, já a classe é apenas uma abstração.  
Na prática, definimos uma classe e, depois, a instanciamos por meio da criação de um objeto. 


## Definindo métodos  
```
class Nome:
    def __init__(self, atributo1, atributo2):  
        self.atributo1 = atributo1  
        self.atributo2 = atributo2  

    def metodo(self):
        comandos
```

# Ok, criamos uma classe e um método... Mas como instânciá-lo?
```
objeto = Nome("Atributo1", "Atributo2")
objeto.metodo()
```


# Herança
Criar classe com base em uma existente, onde a nova classe herdará os atributos e métodos da classe "mãe".  
```
class Mae:
    def __init__(self, atributo):
        self.atributo = atributo
    
    def metodo():
        comando

class Filha(Mae):
```


# Encapsulamento
Ocultar detalhes internos de uma classe.  

_protegido = Uso interno da classe ou subclasse

__privado = dificulta acesso externo direto


Para inserir informações, temos o método `set`.  
Para consultar informações, método `get`.  
Podemos incluir as seguintes anotações para isso:  

```
@property  # para get  
    def metodo(self):  
        comando

@metodo.setter  # para set
    def metodo(self, atributo):  
        self.atributo = atributo
```


# Polimorfismo
Permitir que objetos de diferentes classes respondam de maneira diferente ao mesmo método.  

<br>

---

<br>

# Traduzindo...
É uma boa prática sempre incluir classe com a primeira letra maiúscula.  
`__init__`  -->  construtor da classe. Ele inicializa os atributos que incluirmos a classe.  
`self`  -->  Primeiro parâmetro, por convenção usa-se self, mas ele represent o próprio objeto.  
`atributo1, atributo2` --> Atributos públicos.  
`Filha(Mae)`  -->  Filha herda de Mae


# Método str
Permite definir como os atributos serão apresentados.  
Exemplo:  
```
def __str__(self):
	return f"O {self.marca} {self.modelo} do ano {self.ano}, é um carro de {self.quant_porta} portas e possui velocidade máxima de {self.velocidade_max} km/h"
```

# Método repr
Serve para representarmos um objeto.  
```
def __repr__(self):
    return f"Forma de representar os {atributos}"
```