# Funções recursivas
São funções que chama a si mesma, mas que tem um fim para o problema.  

## Como assim??
- Ela é usada quando um problema pode ser dividido em subproblemas do mesmo tipo.  
- Precisa ter um caso base (caso de parada), que será a consição que interrompe as chamadas recursivas, evitando um loop infinito.  

Um exemplo para entendermos melhor...  
Imagine que faremos um programa que desmonta bonecas russas (aquelas que dentro de uma maior há uma menor, e assim vai indo até chegar em uma bem pequena).  

```
def desmontar(quantidade):
    if quantidade == 0:
        print("fim")
    else:
        print(f'camada {quantidade}')
        desmontar(quantidade - 1)

desmontar(10)
```

O programa iniciará com o valor 10. Quando chegar a quantidade de 0 (não hpuver mais bonecas) ele dirá 'fim'. Mas enquanto essa condição não for verdadeira, ele continuará informando a camada e diminuindo uma, até chegar no caso base.  

(Tem projeto sobre esse conteúdo)
