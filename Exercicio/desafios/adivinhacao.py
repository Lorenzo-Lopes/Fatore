from random import randint

numero_secreto= randint(1,100)
chute = int(input("Digite um numero: "))
tentativas = 0

while chute!= numero_secreto:
    tentativas+=1

    if chute > numero_secreto:
        print(f"O numero secreto é menor que {chute}")
    else:
        print(f'O numero secreto é maior que: {chute}')
    chute = int(input("Digite um numero: "))

print(f'Parabens voce acertou o numero secreto em... {tentativas} tentativas!')
print(f'O numero secreto era: {numero_secreto}')