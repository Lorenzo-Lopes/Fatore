lado1= int(input("Digite o tamanaho em cm: "))
lado2 = int(input("Digite o tamanho do outro lado"))
lado3 = int(input("Digite o tamanho do outro lado"))

if lado1 == lado2 ==lado3:
    print("Equilatero")

elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('isoceles')
elif lado1!= lado2 !=lado3:
    print("escalo")