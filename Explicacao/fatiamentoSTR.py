"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [inicio:fim:passo] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[::1])
print(f"Do inicio até a um ponto: {variavel[:3]}")
print(f"Começando no meio: {variavel[4:]}")
print(f"Pulando letras: {variavel[::2]}")
print(f"Invertendo a ordem: {variavel[::-1]}")