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
    
def get_remainder(number):
    return number % 2


stack = Stack()

def convert_decimal_to_binary(number):
    number // 2

    if number < 2:
        stack.push(get_remainder(number))
        print("resto", get_remainder(number))
        binary = ''
        while not stack.empty():
            binary += str(stack.pop())
        return binary
    else:
        stack.push(get_remainder(number))
        print("resto", get_remainder(number))
        return convert_decimal_to_binary(number//2)


print(convert_decimal_to_binary(int(input("informe o numero "))))
