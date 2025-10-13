def par_impar(numero):
    if numero %2 == 0: 
        return 'Par'
    else:
        return 'Impar'
    

num = int(input('Digite um numero: '))

print(f'O numero digitado {num} é: {par_impar(num)}')