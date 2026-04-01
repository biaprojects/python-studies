# Vamos ao primeiro tópico

Quando pensamos em script, pensamos em

> "Preciso fazer isso acontecer"

Já um sistema...  
- É organizado por responsabilidades
- Separado por camadas
- Extensível
- Reutilizável

Você pensa em:  

> "Quem é responsável por cada parte"

A principal diferença, então, é:
- Script pensa em **fluxo**  
- Sistema pensa em **responsabilidade**


# Organização do código
Quando usar classe, função, módulo, camadas?

## Quando criar uma função?
- É um comportamento isolado
- Não precisa guardar estado
- Não depende de configuração interna
- Pode ser reutilizado como utilitario

Exemplo:
```python
def formatar_cpf(cpf: str) -> str:  
    ...
```

Pergunta mental:  

> Isso precisa “lembrar” de algo entre chamadas?

Se NÃO → função.

Se SIM:

---

## Quando transformar em CLASSE?
- ### Existe estado

Exemplo:
```python
class ConexaoBanco:  
    def __init__(self, host, user, password):  
        self.host = host  
        self.user = user  
        self.password = password
```

Ela guarda dados internos.

- ### Existe responsabilidade agrupada

Se você tem várias funções que trabalham juntas...
```python
def conectar():  
def buscar_dados():  
def salvar_dados():
```

Isso provavelmente vira:
```python
class UsuarioRepository:  
    def conectar()  
    def buscar()  
    def salvar()
```

Porque elas pertencem ao mesmo conceito.

- ### Você pode ter múltiplas instâncias

Exemplo:
```python
Usuario("Beatriz")  
Usuario("João")
```

Cada objeto representa algo diferente.

---

## Quando criar um MÓDULO (arquivo separado)?
- A classe ou grupo de funções já ficou grande
- A responsabilidade está clara
- Você quer isolamento

Exemplo:

repositories/usuario_repository.py  
services/usuario_service.py
