#Peça três notas de um aluno, calcule a média e informe:
#“Aprovado” se média ≥ 7.
#“Recuperação” se média entre 5 e 6.9.
#“Reprovado” se média < 5.

nota1 = float(input("Digite a nota: "))
nota2 = float(input("Digite a nota: "))
nota3 = float(input("Digite a nota: "))
media = (nota1+nota2+nota3)/3
if media >=7: print("Aprovado")
elif media >=5 and media < 7: print("Recuperação")
elif media < 5: print("Reprovado")
else: print("algo deu errado tente novamente")