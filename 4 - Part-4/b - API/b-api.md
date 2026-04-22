# API

Como fazer para consumirmos uma API?

Em Python temos uma lib que serve para fazer requisições HTTP.

Tá... Traduz, por favor...    
Requisições HTTP são mensagens que um usuário envia a um servidor para solicitar ou enviar dados. Elas contém os métodos:   
- GET (para consultar)
- POST (para inserir)
- PUT (para atualizar)
- DELETE (para deletar)  

Além disso, ela precisa de uma URL (como se fosse um endereço que determina o que e onde vamos fazer), cabeçalhos - headers (tokens) e, às vezes, um corpo - body (texto que poderá ser passado do usuário para o sistema).   
Vale lembrar que os headers são no formato de `chave: valor`.   
Depois, o servidor responde com algum código de status (ex: 200 OK, 404 Not found, etc.) e, as vezes, o recurso solicitado.  

Ok, mas afinal, qual é essa lib?  

`requests`

Vamos ver uma demonstração:  

--- 

Digamos que vamos fazer uma consulta.  
- Método: get  
- Será necessário URL  
- Headers (para conseguirmos ter acesso)  
Json não será necessário já que o usuário não enviará nenhum dado.  

```python
# Declarando a URL
url = "minha.url.com/caminho"

# Declarando o(s) header(s)
headers = {
    "nome": "key"
}

# Fazendo, a requisição
response = get.metodo(
    url=url,
    headers=headers
)
```

---

Ok... Mas e se fosse necessário fazer algum cadastro? O cliente precisaria passar dados para o sistema... como isso seria feito?
- Método: post  
- Será necessário URL
- Haders (para conseguir ter acesso)
- Json com os dados

```python
import json 

# Declarando a URL
url = "minha.url.com/caminho"

# Declarando o(s) header(s)
headers = {
    "nome": "key"
}

json = json

# Fazendo, a requisição
response = get.metodo(
    url=url,
    headers=headers,
    json=json
)
```

Isso é:  
`Content-Type: application/json`  
(Dependendo do contexto, é necessário incluir isso no header)

---

Há, também, uma outra forma de se enviar dados.  

`formData`

Ele envia dados para uma API no formato de formulário.  

Ok, mas qual a principal diferença?  
Para Json, fazemos: 
`requests.post(url=url, json=dados)`

Para formData, fazemos:  
`requests.post(url=url, data=dados)`

Outro ponto chave
```python
form_data = {
	"cod_product": cod_product,     
	"name": name,     
	"price": price 
}
```

Isso é:  
(Dependendo do caso)  
`application/x-www-form-urlencoded`  
ou  
`multipart/form-data`  
(É necessário incluir isso no header)


---

## Outro ponto válido!

Como vimos anteriormente, sempre teremos retorno (status, as vezes algum body) e muitas vezes, alguma mensagem de erro.

Então, é uma ótima prática incluir a mensagem e o código que será retornado no print!  

Exemplo: 

```python
print(response.json())  # Vai printar o retorno da requisição em formato list/dict  -> ideal para conseguir trabalhar com o retorno

print(response.text)  # Vai printar o retorno da requisição em forma de String

print(response.status_code)  # Vai printar o código de status
```
