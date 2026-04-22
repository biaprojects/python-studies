
## quando usar classe abstrata (e quando não usar)
Classe abstrata define um contrato. Ela não pode ser instanciada mas obriga subclasses a implementarem certos métodos.  
Em python, usamos o módulo `abc` para isso.  

Exemplo:
```python
from abc import ABC, abstractmethod

class Pagamento(ABC):
	@abstractmethod
	def pagar(self, valor):
		pass
```

Traduzindo...
> qualquer classe que herdar de pagamento é obrigada a implementar pagar.

E quando realmente usar?
- Você tem multiplas implementações possiveis... ou seja, Existe um **comportamento comum**, mas **formas diferentes de executá-lo**.
	Exemplo:
	- Pagamento via pix
	- Pagamento via cartão
	- Pagamento via boleto

	Todos fazem "pagar", mas de forma diferente...  
	Nesse caso... faz sentido:  
	- class Pix(Pagamento)
	- class Cartao(Pagamento)
	- class Boleto(Pagamento)
	
	```python
	from abc import ABC, abstractmethod
	
	class Pagamento(ABC):
    @abstractmethod
	    def pagar(self, valor):
	        pass
        
        
    class Pix(Pagamento):
	    def pagar(self, valor):
	        print(f"Pagando {valor} via Pix")
	```
	(isso é polimorfismo)
	
- quando quer desacoplar a regra de negócio... porque a regra de negócio não deve depender de tecnologia.
	Exemplo:  
	salvar usuários
	Você pode salvar em PostgreSQL, MongoDB, API externa, Arquivo, DynamoDB...
	Mas a **regra de negócio não deveria saber disso**.
	exemplo:
	- Forma acoplada (errada)
		```python
		class UsuarioService:  
		    def salvar_usuario(self, usuario):  
		        repo = PostgresUsuarioRepository()  
		        repo.salvar(usuario)
		```
	Problema:
	O Service **depende do banco**.
	Se mudar o banco, o Service muda.
	- Forma desacoplada (correta)
		Primeiro criamos o contrato.
		```python
		from abc import ABC, abstractmethod  
		
		class UsuarioRepository(ABC):  
		@abstractmethod
		def salvar(self, usuario):
			pass
		### Implementação Postgres
		
		class PostgresUsuarioRepository(UsuarioRepository):  
			def salvar(self, usuario):
			print("Salvando no Postgres")
		```


### Service agora depende da abstração

class UsuarioService:  
  
    def __init__(self, repository: UsuarioRepository):  
        self.repository = repository  
  
    def salvar_usuario(self, usuario):  
        self.repository.salvar(usuario)

Agora o Service **não sabe qual banco está sendo usado**.
- quando quer forçar padrão arquitetural


## NÃO use Classe Abstrata Quando...
### - Existe apenas uma implementação
Se você só tem:

class UsuarioRepository:

E não existe possibilidade real de ter outra implementação…

Criar abstrata só por “arquitetura bonita” é overengineering.

### - Você não precisa trocar implementação

Se o código nunca vai mudar de tecnologia, não complique.

### - Você ainda está explorando o domínio

Durante fase inicial, abstração prematura atrapalha.
