# 1ª solução
##############################################
numero = int(input("Digite um numero: "))

centena = numero // 100
dezena = (numero //10 )%10
unidade = numero %10
print(centena,dezena,unidade)

if unidade > dezena and unidade> centena:
    print(f'o maior digito é {unidade}')
elif dezena> unidade and dezena >centena:
    print(f'o maior digito é {dezena}')
elif centena > unidade and centena > dezena:
    print(f'O maior digito é: {centena}')

#2ª solulação
# numero = input("Digite um numero: ")
# lista_numero = []

# for digito in numero:
#     lista_numero.append(digito)

# print(max(lista_numero))