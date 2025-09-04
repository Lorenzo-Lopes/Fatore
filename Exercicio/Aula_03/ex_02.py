# Peça a idade do usuário e informe:
# Se for menor de 12 anos, exibir “Criança”.
# Se for entre 12 e 17 anos, exibir “Adolescente”.
# Se for 18 anos ou mais, exibir “Adulto”.

idade = int(input("Informe sua idade: "))

if idade <12:
    print(f"Voce tem {idade} e ainda é Criança")
elif idade<18:
    print(f"Voce tem {idade} e é um adolescente")
else:
    print(f"Vote tem {idade} e é adulto")