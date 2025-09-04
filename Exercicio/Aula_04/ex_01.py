#Peça ao usuário um número e mostre a tabuada dele de 1 a 10.

tab = int(input("Insira o numero que voce deseja saber a tabuada: "))
i=1
for i in range(10):
    print(f"{tab} x {i+1} = {tab*(i+1)}")