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

#

Agora vem uma parte crítica...  
Erro comum na transição:  
Criar classe para TUDO.

Isso gera:

- Classes utilitárias desnecessárias
- Estado onde não deveria existir
- Código mais complexo do que precisa

Então...  
**Pergunta que decide tudo**

Antes de criar uma classe, pergunte:
1. Isso tem estado?
2. Isso representa um conceito?
3. Isso tem responsabilidade própria?
4. Isso pode ter múltiplas implementações no futuro?

Se a maioria for “não” → provavelmente é função.

# 

## Uma estutura típica para sistema:

project/
| 
|-- main.py
|-- controllers/
|-- services/
|-- repositories
|-- models


### main.py 
O “ponto de partida”. Arquivo com o fluxo geral, onde o sistema começa a rodar.  

Responsabilidades: 
- Orquestrar o sistema
- Carregar configurações
- Iniciar dependências
- Iniciar loop principal

Não cabe a ele: 
- Conter regras de negócio 
- Se comunicar com banco de dados


### controllers
A "porta". São os arquivos que conversam com o usuário.  

Responsabilidades:
- Receber as requisições
- Interpretar o pedido
- Realizar a validação inicial (se todos os campos obrigatórios foram preenchidos, por exemplo)
- Delegar o trabalho
- Responder o usuário  

Não cabe a ele:
- Acessar o banco de dados;
- Conter regra de negócio complexa.


### services/
o cérebro. Arquivo onde estão as regras de negócio. 

Responsabilidades: 
- Orquestração (coordena as ações, chamando métodos de repository); 
- Regra de negócios (ex: não ter ID repetido);
- Transações (solicita as transações no banco de dados).  

Não cabe a ele:
- Conhecer métodos HTTP (função do controller)
- Executar diretamente os comados no banco.

### repositories
Essa camada é responsável exclusivamente por acessar o banco de dados.

Responsabilidades:
- Inserir dados
- Buscar dados
- Atualizar dados
- Deletar dados

Não cabe a ele:
- Validar regra de negócio
- Decidir se algo pode ou não acontecer
- Interpretar requisições HTTP

### models
Os "moldes". Aqui ficam as representações das entidades do sistema, representando um objeto do domínio.

Em alguns frameworks também podem validar dados, por exemplo.
