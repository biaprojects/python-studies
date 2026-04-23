Em algumas situações, temos a seguinte dificuldade...  
-> Saber o que estava sendo executado por último e para onde voltar caso uma função seja interrompida

Solução: 
# Pilha
**Definição:** estrutura para armazenar conjunto de elementos  

**Estrutura:**  
- Novos elementos sempre entram no topo  
- O único elemento que pode ser retirado é o do topo  

**Principais usos:** Situações onde precisamos guardar elementos "para mais tarde" e precisamos sempre lembrar do último armazenado.


## Exercício
Implementar um programa que realiza a conversão de um número decimal para binário usando pilha para armazenar os valores dos restos

Lembrando: A lógica para realizar esse cálculo é:
- Divide o número por 2 e vai dividindo os quocientes por 2 até chegar a um quociente 0.
- Guarda os restos
- Inverte os restos

Então, por exemplo (sempre dividindo por 2)...
VALOR => 13 -> 6 -> 3 -> 1
RESTOS => 1 -> 0 -> 1 -> 1

O número decimal *13* em binário é *1101* 


## resolução em aula (a minha está no código)
```python
class Stack():
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)
    
    def pop(self):
        if len(self.data) > 0:
            return self.data.pop(-1)
        
    def top(self):
        # Consulta último elemento da pilha
        if len(self.data) > 0:
            return self.data(-1)
        
    def empty(self):
        return not len(self.data)
    
    def get_data(self):
        return self.data


stack = Stack():
num = 13
while num > 0:
    resto = num % 2
    num = num // 2
    stack.push(resto)

while not stack.empty():
    print(p.pop())
```
