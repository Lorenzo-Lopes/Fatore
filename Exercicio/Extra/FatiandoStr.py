"""
Exercício
Peça ao usuário para digitar seu nome / Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
outracoisa = input("Digite seu Nome: ")
idade = input("Digite sua idade: ")

if outracoisa and idade :
    print(f"O nome informado foi: {outracoisa}")
    print(f"O nome invertido fica : {outracoisa[::-1]}")
    if ' ' in outracoisa:
        print(f"O seu nome tem {outracoisa.count(' ')} espaços!")
    else:
        print("Seu nome nao contem espaços")
    print(f'O nome informado tem um total de {len(outracoisa)} letras')
    print(f"A primeira letra do nome informado é : {outracoisa[0]}")
    print(f"A ultima letra do nome informado é : {outracoisa[-1]}")
else: 
    print("Voce deixou algum campo vazio.")