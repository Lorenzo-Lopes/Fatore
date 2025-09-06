#Peça o valor da compra e a forma de pagamento:
#“À vista” → 10% de desconto.
#“Cartão em 2x” → preço normal.
#“Cartão em 3x ou mais” → 10% de acréscimo.

print('Calculo de Pagamento')

valor = float(input("Informe o valor da compra: "))

print ("Informe a forma de pagamento:  \n 1) A  vista \n 2) 2x no Cartão \n 3) 3x ou mais vezes no cartão" )

forma_pgnt = int(input("Digite sua forma de pagamento aqui: "))

if forma_pgnt == 1:
    valor_final = valor-(valor*0.1)
elif forma_pgnt == 2:
    valor_final = valor
elif forma_pgnt == 3:
    valor_final = valor+(valor*0.1)

print(f"O valor final da compra é de {valor_final} ")

