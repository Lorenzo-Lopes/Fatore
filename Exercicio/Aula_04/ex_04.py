#O programa sorteia um número(por exemplo,7) O usuário deve tentar adivinhar até acertar.

#import random
#sorteio = random.randint(1,10)
from random import randint
sorteio = randint(1,10)
opc = int(input("Digite um numero para tentar acertar: "))

while opc != sorteio:
    print("errou tente novamente")
    opc = int(input("Digite um numero para tentar acertar: "))
print (f"Parabens voce acertou o numerto sorteado era {sorteio}")