# Pesquisa binária
A pesquisa binária (ou busca binária) é um algoritmo eficiente para encontrar um elemento em uma lista **ordenada**. Isso funciona dividindo repetidamente a lista pela metade até encontrar o valor desejado ou concluir que ele não está presente.  
  
## Como funciona?
1. Começa com 2 ponteiros, um no início e outro no final da lista.  
2. Calcula o meio `(inicio + fim) // 2`  
3. Compara o valor do meio com o valor buscado...  
    - Se for igual, encontrou.  
    - Se o valor do meio for maior, repete a busca na metade esquerda.
    - Se for menor, repete a busca na metade direita.  
4. O processo continua até encontrar o valor ou até que o intervalo da busca se torne inválido (`início > fim`).


IMPORTANTE!    
A lista precia estar ordenada!


Exemplo:  
```
def pesquisa_binaria(lista, alvo):
    inicio, fim = 0, len(lista) -1      # poderia ser dividido em 2 linhas também (inicio = 0  |  fim = len(lista) -1)
    
    while inicio <= fim:
        meio = (inicio + fim) // 2      # Encontrar o meio
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1       # Elemento não encontrado
```


## E se eu juntar pesquisa binária com recursividade?

```
def busca_binaria_rec(lista, alvo, inicio, fim):
    if inicio > fim:
        return -1

    meio = (inicio + fim) // 2
    if lista[meio] == alvo:
        return meio
    elif lista[meio] < alvo:
        return busca_binaria_rec(lista, alvo, meio + 1, fim)
    else:
        return busca_binaria_rec(lista, alvo, inicio, meio - 1)
```
