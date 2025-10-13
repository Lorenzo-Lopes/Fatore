def verifica_primo(n):
    if n <2:
        return False
    for i in range (2, int(n ** 0.5 ) + 1):
        if n % i == 0:
            return False
    return True
        
for numero in range (1,21):
    print (f'{numero} é primo?',verifica_primo(numero))


