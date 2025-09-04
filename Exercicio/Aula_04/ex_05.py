#Peça um número inicial e faça uma contagem regressiva até zero.
import time
contador = int(input("Digite um numero: "))

while contador > 0:
    print(f"A contagem termina em: {contador} segundo.")
    time.sleep(1)
    contador-=1

print("BUUUUM!!!!")