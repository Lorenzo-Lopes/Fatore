import os
from time import sleep
import getpass

class jogador():

    def __init__(self, vida, defesa, ataque,pocao):
        self.vida =     vida
        self.defesa =   defesa
        self.ataque =   ataque
        self.pocao =    pocao

p1 =jogador(100,100,25,2)
p2=jogador(100,100,25,2)

# def start_combat():
#     while p1.vida>0 or p2.vida>1:
#         print('Jogador 1: Digite 1-ataque | 2-Defender| 3- Curar')
#         acaoP1 = input('Digite sua Ação: ')
#         os.system('clear')
#         print('Jogador 2: Digite 1-ataque | 2-Defender| 3- Curar')
#         acaoP2 = input('Digite sua Ação: ')
#         print("Ações registradas. Iniciando combate.")
#         for i in range(3):
#             print('. ',end='')
#             sleep(0.5)
#             print("\n")
        
def p1_action():
    op1 = int(getpass.getpass("Jogador 1: Qual vai ser sua ação?"))
    os.system('clear')
    return op1

def p2_action():
    op2 = int(getpass.getpass("Jogador 2: Qual vai ser sua ação?"))
    os.system('clear')
    return op2

while p1.vida or p2.vida: 
    op1= p1_action()
    op2=p2_action()
    print("teste")


    if op1 == 1 and op2 == 1:
        p1.vida -= p2.ataque
        p2.vida -= p1.ataque
        print(f'Jogador 1 atacou o Jogador 2 e causou {p1.ataque} de dano')
        print(f'Jogador 2 atacou o Jogador 1 e causou {p2.ataque} de dano')

    elif op1 == 1 and op2 == 2:
        dano = p1.ataque - p2.defesa
        if dano < 0:
            dano = 0
        p2.vida -= dano
        print(f'Jogador 1 atacou o Jogador 2 e causou {dano} de dano')  
    elif op1 == 2 and op2 == 1:
        dano = p2.ataque - p1.defesa
        if dano < 0:
            dano = 0
        p1.vida -= dano
        print(f'Jogador 2 atacou o Jogador 1 e causou {dano} de dano')
    
    elif op1 == 2 and op2 == 2:
        print('Ambos os jogadores defenderam. Nenhum dano foi causado.')
    elif op1 == 3 and op2 == 1:
        if p1.pocao > 0:
            p1.vida += 20
            p1.pocao -= 1
            print('Jogador 1 usou uma poção e recuperou 20 de vida.')
        p1.vida -= p2.ataque
        print(f'Jogador 2 atacou o Jogador 1 e causou {p2.ataque} de dano')
    elif op1 == 1 and op2 == 3:
        if p2.pocao > 0:
            p2.vida += 20
            p2.pocao -= 1
            print('Jogador 2 usou uma poção e recuperou 20 de vida.')
        p2.vida -= p1.ataque
        print(f'Jogador 1 atacou o Jogador 2 e causou {p1.ataque} de dano')
    elif op1 == 3 and op2 == 2:
        if p1.pocao > 0:
            p1.vida += 20
            p1.pocao -= 1
            print('Jogador 1 usou uma poção e recuperou 20 de vida.')
        print('Jogador 2 defendeu. Nenhum dano foi causado.')
    elif op1 == 2 and op2 == 3:
        if p2.pocao > 0:
            p2.vida += 20
            p2.pocao -= 1
            print('Jogador 2 usou uma poção e recuperou 20 de vida.')
        print('Jogador 1 defendeu. Nenhum dano foi causado.')
    elif op1 == 3 and op2 == 3:
        if p1.pocao > 0:
            p1.vida += 20
            p1.pocao -= 1
            print('Jogador 1 usou uma poção e recuperou 20 de vida.')
        if p2.pocao > 0:
            p2.vida += 20
            p2.pocao -= 1
            print('Jogador 2 usou uma poção e recuperou 20 de vida.')
    print(f'Vida Jogador 1: {p1.vida} | Vida Jogador 2: {p2.vida}')
    print(f'Poções Jogador 1: {p1.pocao} | Poções Jogador 2: {p2.pocao}')
    print('-----------------------------------')
    
    if p1.vida <=0 and p2.vida <= 0:
        print("EMPATE")
    elif p1.vida <= 0:
        print('Jogador 2 Venceu!')
        break
    elif p2.vida <= 0:
        print('Jogador 1 Venceu!')
        break
    
