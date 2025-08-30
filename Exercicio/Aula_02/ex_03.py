#Crie uma lista de compras. Permita adicionar itens até que o usuário digite "sair". No final, mostre a lista completa.
lista_compras=[]

item=""

while item != "sair":
    item = input("Digite o produto.")
    lista_compras.append(item)
 
    

print(lista_compras)