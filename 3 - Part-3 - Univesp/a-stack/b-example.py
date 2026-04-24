class Pilha():
    def __init__(self):
        self.data = []

    def push(self, element):
        # Adiona novo elemento à pilha
        self.data.append(element)
    
    def pop(self):
        # Remove último elemento da pilha
        if len(self.data) > 0:
            return self.data.pop(-1)
    
    def top(self):
        # Consulta último elemento da pilha
        if len(self.data) > 0:
            return self.data(-1)
        
    def empty(self):
        # Retorna True para pilha vazia e False quando há elementos
        return not len(self.data)
    
# instanciar uma pilha
p = Pilha()
p.push(4)
p.push(5)
p.push(6)

# desempilhar um elemento dessa pilha
p.pop()
