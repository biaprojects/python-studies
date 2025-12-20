E se formos ler uma API, commo fazer?

Em Python temos uma lib de para fazer requisições HTTP.

Tá... Será que dá para traduzir?  
Requisições HTTP são mensagens que um usuário envia a um servidor para solicitar ou enviar dados. Elas contém os métodos:  
- GET (para consultar)
- POST (para inserir)
- PUT (para atualizar)
- DELETE (para deletar)  

Além disso, ela precisa de uma URL (como se fosse um endereço que determina o que e onde vamos fazer), cabeçalhos - headers (tokens) e, às vezes, um corpo - body (texto que poderá ser passado do usuário para o sistema).  
Vale lembrar que os headers são no formato de `chave: valor`  
Depois, o servidor responde com algum código de status (ex: 200 OK, 404 Not found, etc.) e, as vezes, o recurso solicitado.  

Ok, mas afinal, qual é essa lib?  

`requests`

Então... o que podemos fazer?

```python
# Declarando a URL
url = "minha.url.com/caminho"

# Declarando o(s) header(s)
headers = {
    "nome": "key"
}

# Caso precise de um json:
json = json

# Fazendo, a requisição
response = requests.metodo(
    url=url,
    headers=headers,
    json=json
)

```