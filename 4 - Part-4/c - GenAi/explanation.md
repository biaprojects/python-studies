# GenAi

Qual é o fluxo da interação?  

Python → SDK → API do modelo → Resposta → Python

Você não executa o modelo localmente, você chama uma API.  
Exemplo:   
`requests.post("endpoint-do-modelo", payload)`

#

### Vamos criar o ambiente virtual
No terminal, dentro do seu projeto:

1. No terminal, dentro do seu projeto:  
    `python -m venv .venv`  
    *(Se usar WSL, Linux, Ubuntu, talvez seja necessário rodar antes...*  
    *`sudo apt update`*  
    *`sudo apt install python3.12-venv`)*  

    Ative:  
    Windows: `.venv\Scripts\activate`  
    Linux: `source .venv/bin/activate`

    Se for Fish (ainda mais específico): `source .venv/bin/activate.fish`  

    Isso evita conflitos (muito importante quando começar a usar libs de IA).

2. Instale o SDK e dependências necessárias  
    Vamos usar o SDK oficial:
    `pip install openai`

### Pegando credencial (API Key)
Será necessário o uso de uma API Key.  

### Boa prática!
Não é uma boa prática fazer:  
`api_key = "minha-chave"`  

Faça assim:  
Variável de ambiente fica em 
`.env`

Exemplo de .env:   
`OPENAI_API_KEY=xxxxxx`  

E no código:
`import os`
`os.getenv("OPENAI_API_KEY")`

#

### Vamos de exemplo?  
```python
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-mini",
    input="Explique o que é GenAI em uma frase simples"
)

print(response.output_text)
```

O que está acontecendo aqui (linha por linha):  

`from openai import OpenAI`  
→ importa o cliente da API

`client = OpenAI()`
→ cria um cliente usando a API Key do ambiente

`model="gpt-4.1-mini"`
→ escolhe um modelo leve (ótimo para começar)

`input="Explique o que é GenAI..."`
→ isso é o prompt

`response.output_text`
→ texto final já tratado (sem você precisar navegar em JSON)

#### Resultado esperado

No terminal, algo como:

GenAI é uma tecnologia que cria novos conteúdos, como textos e códigos, a partir de padrões aprendidos em grandes volumes de dados.
