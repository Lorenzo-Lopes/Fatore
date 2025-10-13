# def conta_vogais_a(frase):
#     cont_a = 0
#     a = 'aA'
    
#     for letra in frase:
#         if letra in a:
#             cont_a +=1
#     return cont_a

# def conta_vogais_e(frase):
#     cont_e = frase.count('e' )
#     cont_e += frase.count('E')

#     return cont_e

# def conta_vogais_i(frase):
#     cont_i = frase.count('i' )
#     cont_i += frase.count('I')

#     return cont_i

# def conta_vogais_o(frase):
#     cont_o = frase.count('o' )
#     cont_o += frase.count('O')

#     return cont_o
# def conta_vogais_u(frase):
#     cont_u = frase.count('u' )
#     cont_u += frase.count('U')

#     return cont_u

# ###################################################################

# frase = input('Digite uma frase e contaremos as repetições de cada vogal que aparecer:  ')

# vezes_a = conta_vogais_a(frase)
# vezes_e = conta_vogais_e(frase)
# vezes_i = conta_vogais_i(frase)
# vezes_o = conta_vogais_o(frase)
# vezes_u = conta_vogais_u(frase)

# print (f'A letra A apareceu {vezes_a} vezes')
# print (f'A letra E apareceu {vezes_e} vezes')
# print (f'A letra E apareceu {vezes_i} vezes')
# print (f'A letra E apareceu {vezes_o} vezes')
# print (f'A letra E apareceu {vezes_u} vezes')

#######################################################################################################################################################################


def conta_vogais(frase):
    lista = [0,0,0,0,0]

    for letra in frase():
        if letra == 'a':
            lista[0] = frase.count('a')
        elif letra == 'e':
            lista[1] = frase.count('e')
        elif letra == 'i':
            lista[2] = frase.count('i')
        elif letra == 'o':
            lista[3] = frase.count('o')
        elif letra == 'u':
            lista[4] = frase.count('u')
    return lista

frase = input('Digite uma frase e contaremos as repetições de cada vogal que aparecer:  ')

aeiou= conta_vogais(frase.lower())


print (f'A letra A apareceu {aeiou[0]} vezes')
print (f'A letra E apareceu {aeiou[1]} vezes')
print (f'A letra I apareceu {aeiou[2]} vezes')
print (f'A letra O apareceu {aeiou[3]} vezes')
print (f'A letra U apareceu {aeiou[4]} vezes')

