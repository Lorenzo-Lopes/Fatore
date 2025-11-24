numero = int(input("Digite um numero: "))

centena = numero // 100
dezena = (numero //10 )%10
unidade = numero %10
numero_invertido= (unidade*100)+(dezena*10)+centena

print(numero_invertido)