# nota_100    = 0
# nota_50     = 0
# nota_20     = 0
# nota_10     = 0
# nota_5      = 0
# nota_1      = 0

# valor_saque = int(input("Quanto deseja sacar?"))
# sacado = 0

# while sacado < valor_saque:
#     if (valor_saque-sacado)>=100:
#         nota_100 +=1
#         sacado+=100
#         continue
#     elif (valor_saque-sacado)>=50:
#         nota_50+=1
#         sacado+=50
#         continue
#     elif (valor_saque-sacado)>=20:
#         nota_20+=1
#         sacado+=20
#         continue
#     elif (valor_saque-sacado)>=10:
#         nota_10 +=1
#         sacado+=10
#         continue
#     elif (valor_saque-sacado)>=5:
#         nota_5+=1
#         sacado+=5
#         continue
#     elif (valor_saque-sacado)>=1:
#         nota_1 +=1
#         sacado+=1
#         continue
# print("O saque foi realizado com sucesso")
# print(f"total sacado de {sacado}")

# print(f'notas de 100: {nota_100}')
# print(f'notas de 50: {nota_50}')
# print(f'notas de 20: {nota_20}')
# print(f'notas de 10: {nota_10}')
# print(f'notas de 5: {nota_5}')
# print(f'notas de 1: {nota_1}')




valor_saque = int(input("Quanto deseja sacar?"))
resto = valor_saque

notas = [100,50,20,10,5,1]
qtd = []

for nota in notas:
    qtd.append((resto//nota))
    resto=resto%nota

print("Saque realizado com sucesso!")
print(f"Valor total sacado: {valor_saque}")

for nota in range(len(notas)):
    print(f"Notas de {notas[nota]}: {qtd[nota]}")
