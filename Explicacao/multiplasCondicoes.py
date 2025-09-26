x="""Digamos que eu queria comprar algo, porem para comprar eu preciso ter dinheiro para isso ou o item precisa estar em promoção"""

dinheiro_guardado = int(input("Informe quanto voce tem guardado: "))
valor_item = 120
promocao = False

if promocao==True:
    valor_item=valor_item-valor_item*0.2
    

if dinheiro_guardado >= valor_item and promocao == True:
    print("Voce vai poder comprar o item com valor promocional")

elif dinheiro_guardado>= valor_item and promocao==False:
    print("Voce vai poder comprar o item fora da promoção")
else:
    print("Voce precisa guardar mais dinheiro para comprar o item")


