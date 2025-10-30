import random 
def Escolhe_Palavra():
    with open('palavras.txt', 'r') as f:
        palavras = f.readlines()
        pass
    escolha = palavras[random.randint(0,(len(palavras)-1))][0:-1:].upper()
    return escolha

def mostra_espaços(palavra):
    print('__ '*len(palavra))


def recebe_chute():
    chute= input('Digite uma letra ou tente acertar a palavra secrete: ')
    return chute

def verifica_chute(chute,palavra_secreta):
    posicoes = []
    start = 0
    while True:
        start = palavra_secreta.find(chute.upper(), start)
        if start == -1:
            break
        posicoes.append(start)
        start += 1 # Começa a busca a partir da próxima posição

    return(f"As posições da letra 'a' são: {posicoes}")
            

palavra_secreta= Escolhe_Palavra()
chute  = recebe_chute()
print(palavra_secreta)
mostra_espaços(palavra_secreta)

print(verifica_chute(chute,palavra_secreta), 'aaaaaaaaaaaaaaaa')