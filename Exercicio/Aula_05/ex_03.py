def cria_lista():
    lista = []
    for i in range(5):
        lista.append(int(input("Digite um numero: ")))
    return lista
def verificar_maior(lista_numero):
    maior = lista_numero[0]

    for numero in lista_numero:
        if numero > maior:
            maior = numero
    return maior


lista = cria_lista()

maior = verificar_maior(lista)

print(f'O maior numero da lista é: {maior}')