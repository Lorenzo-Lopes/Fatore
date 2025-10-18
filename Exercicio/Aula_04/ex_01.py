#Peça ao usuário um número e mostre a tabuada dele de 1 a 10.

tab = int(input("Insira o numero que voce deseja saber a tabuada: "))
for i in range(1,11):
    print(f"{tab} vezes {i} = {tab*(i)}")