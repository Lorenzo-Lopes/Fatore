palavra= input("Digite uma palavra: ")

invertida = []
str_invertida=''
for letra in palavra:
    invertida.insert(0,letra)
for letra in invertida:
    str_invertida+=letra

# palavra= input("Digite uma palavra: ")
# str_invertida = palavra[::-1]
    
# if palavra == str_invertida:
#     print(f'{palavra} é um PALINDROMO')
# else:
#     print("Nao é um palindromo.")