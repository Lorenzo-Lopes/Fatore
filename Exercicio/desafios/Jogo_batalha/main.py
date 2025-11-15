import os
from time import sleep
class jogador():

    def __init__(self, vida, defesa, ataque,pocao):
        self.vida =     vida
        self.defesa =   defesa
        self.ataque =   ataque
        self.pocao =    pocao

player1 =jogador(100,100,15,3)
player2 =jogador(100,100,15,3)

def start_combat():
    while player1.vida>0 or player2.vida>1:
        print('Jogador 1: Digite 1-ataque | 2-Defender| 3- Curar')
        acaoP1 = input('Digite sua Ação: ')
        os.system('clear')
        print('Jogador 2: Digite 1-ataque | 2-Defender| 3- Curar')
        acaoP2 = input('Digite sua Ação: ')
        print("Ações registradas. Iniciando combate.")
        for i in range(3):
            print('. ',end='')
            sleep(0.5)
            print("\n")
        
start_combat()