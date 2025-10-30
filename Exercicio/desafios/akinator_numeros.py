print("Vamor jogar um jogo de adivinhação, as regras são as seguintes\n" \
"1ª - Pense num numero de 1 a 100\n" \
"2ª - Quando eu chutar um numero voce precisa responter com: 1 se o numero for maior ou 2 se for menor\n" \
"3ª - Quando eu acertar digite 3 para finalizar o jogo")

inicio_fim_chutes = [0,101]
chute = 50
tentativas = 1
print(f'1- maior | 2- menor | 3- acertou!! >>>> Meu {tentativas}º chute é: {chute}')
tentativas+=1
lista_chutes=[]

opc = int(input("Digite uma opção: "))

while True:
    lista_chutes.append(chute)
    tentativas+=1
    if opc ==1:
        inicio_fim_chutes[0] = chute
    elif opc == 2: 
        inicio_fim_chutes[1] = chute
    elif opc == 3:
        break
    else:
        print('numero digitado invalido.')
        opc = int(input("Digite uma opção: "))
        continue
    
    chute= sum(inicio_fim_chutes )//2
    print(f'1- maior | 2- menor | 3- acertou!! >>>> Meu {tentativas}º chute é : {chute}')

    opc = int(input("Digite uma opção: "))

print(f'O numero era: {chute} e acertei em {tentativas} tentativas')
print(f"Os numeros chutados foram: {lista_chutes}")