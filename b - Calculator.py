import time

print("Iniciando sua calculadora com termos matemáticos!")
time.sleep(2)

print("Digite o número da operação que deseja realizar")
print("1 -> soma\n"
      "2 -> subtração\n"
      "3 -> multiplicação\n"
      "4 -> divisão\n"
      "5 -> divisão inteira\n"
      "6 -> resto da divisão\n"
      "7 -> exponenciação")
operacao = int(input())

print("Agora digite: ")
if operacao == 1:
    numero1 = int(input("Primeiro termo "))
    numero2 = int(input("Segundo termo "))
    print("A soma é:", numero1 + numero2)
elif operacao == 2:
    numero1 = int(input("Minuendo "))
    numero2 = int(input("Subtraendo "))
    print("A diferença é:", numero1 - numero2)
elif operacao == 3:
    numero1 = int(input("Primeiro fator "))
    numero2 = int(input("Segundo fator "))
    print("O produto é:", numero1 * numero2)
elif operacao == 4:
    numero1 = int(input("Dividendo "))
    numero2 = int(input("Divisor "))
    if numero2 == 0:
        print("Não é possível dividir por 0")
    else:
        print("O quociente é:", numero1 / numero2)
elif operacao == 5:
    numero1 = int(input("Dividendo "))
    numero2 = int(input("Divisor "))
    if numero2 == 0:
        print("Não é possível dividir por 0")
    else:
        print("O quociente inteiro é:", numero1 // numero2)
elif operacao == 6:
    numero1 = int(input("Dividendo "))
    numero2 = int(input("Divisor "))
    if numero2 == 0:
        print("Não é possível dividir por 0")
    else:
        print("O resto da divisão é:", numero1 % numero2)
elif operacao == 7:
    numero1 = int(input("Base "))
    numero2 = int(input("Expoente "))
    print("A potência é:", numero1 ** numero2)
else:
    print("Operação inválida!")