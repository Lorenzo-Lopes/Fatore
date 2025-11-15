fibonacci =[0,1]
qtd_sequencia= int(input('Quantos numero da sequencia de Fibonacci deseja ver? '))

for n in range(qtd_sequencia):

    fibonacci.append(fibonacci[-1]+fibonacci[-2])
    print(fibonacci[n])
