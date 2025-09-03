#Peça dois números e uma operação (+, -, *, /). Mostre o resultado conforme a operação escolhida.

num1 = int(input("Digite um  numero "))
num2 = int(input("Digite outro numero"))

print("Selecione uma operação : 1)Adição | 2)Subtração | 3)Multiplicação | 4)Divisão")

operaçao= int(input("= "))

if operaçao ==1:
    print(num1 + num2)
elif operaçao == 2:
    print(num1 - num2)
elif operaçao == 3:
    print(num1 * num2)
elif operaçao == 4:
    print(num1 / num2)
else:
    print('Operação invalida, tente denovo')