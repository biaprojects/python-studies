Bom... Já vimos como definir nossa própria função (através do método `def`) mas, e para definirmos uma classe com atributos e métodos?  

# Definindo classe  
Sintaxe:  
```  
class Nome: 
    def __init__(self, atributo1, atributo2):  
        self.atributo1 = atributo1  
        self.atributo2 = atributo2  
```

E os métodos?

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


# Criando pacote
Abra um diretório (pasta) e ccrie um arquivo com o nome `__init__`.    
Para importar para fora do pacote, teria que referenciar todo o caminho, como...
```
import nome_pacote.nome_arquivo
nome_pacote.nome_arquivo.nome_funcao()
```

Mas... tem como "encurtar" isso...

```
from nome_pacote.nome_arquivo import nome_funcao()
nome_funcao()
```

# Método str
Permite definir como os atributos serão apresentados.  
Exemplo:  
```
def __str__(self):
	return f"O {self.marca} {self.modelo} do ano {self.ano}, é um carro de {self.quant_porta} portas e possui velocidade máxima de {self.velocidade_max} km/h"
```
