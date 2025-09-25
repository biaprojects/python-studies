Ok... vimos que python tem algumas funções pré definidas como...
| código | função | 
| :---: | :---: |
| len() | tamanho |
| ord() | recebe um caractere e retornao valor numerico correspondente ao UNICODE |
| chr() | recebe valor numérico unicode e retorna o correspondente caractere | 


### Mas... o que é uma função?
Funções são blocos de código reutilizáveis que executam uma tarefa específica. Elas ajudam a tornar seu código mais organizado, reutilizável e legível.


### E se eu quiser definir a minha própria?  

<br>

# def
Sintaxe:  
```
def funcao(parametros):
    comando
```

Ela pode ser uma função que executa uma ação.  
Ex: 
```
def saudar(nome):
    print(f"Olá, {nome!}")
```

Mas também pode ser uma função que retorna algum valor...  
```
def soma(valor1, valor2):
    return valor1 + valor2
```

Explicando...  
- `def` = inicia uma definição de função;
- `saudar`, `soma` = nome da função
- `(nome)`, `(valor1, valor2)` = parâmetros que a função espera receber;
- `print`, `return` = são as ações da função..
