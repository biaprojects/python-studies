
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
