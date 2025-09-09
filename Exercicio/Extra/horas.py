
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horas_informadas = input("Que horas são?  ")

try:
    agora = int(horas_informadas)
    
    if agora >= 00 and agora <=11:
        print("Bom Dia!!")
    elif agora >=12 and agora<=17:
        print("Boa tarde!!")
    elif agora >=18 and agora <=23:
        print("Boa Noite!!")
    else:
        print("A hora informada é invalida.")
except:
    print("Horario informado é invalido, verifique e tente novamente.")