concatenacao = 'Lorenzo' + ' ' + 'Lopes'
print(concatenacao)

a_dez_vezes = 'A' * 50
tres_vezes_lorenzo = 3 * 'Lorenzo'
print(a_dez_vezes)
print(tres_vezes_lorenzo)

n1 = 10 
n2 = 20 
n3 = 30 

#concatenando usando fstring
print(f'isso é um numero : {n1}, concatenado com o numero {n2}, logo em seguida o {n3}')

# concatenando usando .fortmat
print('isso é um numero : {}, concatenado com o numero {}, logo em seguida o {}'.format(n1,n2,n3))