"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero = input("Informe a diametro de um circulo para calcularmos a area:")

try:
    diametro = float(numero)
    raio = diametro/2
    area = (raio**2)*3.14
    print(f"A area calculada foi: {area}")
except:
    print("O valor informado nao é um numero!")