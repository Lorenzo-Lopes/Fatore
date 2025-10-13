import getpass
def verifica_tamanho_senha(senha):
    if len(senha) <8:
        return False
    else:
        return True
def verifica_num_senha(senha):
    numeros = '1234567890'
    for letra in senha:
        if letra in numeros:
            return True
    return False

def verifica_maiuscula_senha(senha):
    for letra in senha:
        if letra.isupper():
            return True
    return False
    
senha = getpass.getpass("Digite sua senha: ")
tam_senha= verifica_tamanho_senha(senha)
tem_num = verifica_num_senha(senha)
tem_maiuscula= verifica_maiuscula_senha(senha)

if tam_senha and tem_num and tem_maiuscula:
    print("Senha aprovada!!")

elif tam_senha==False or tem_num== False or tem_maiuscula==False:
    if tam_senha == False:
        print("A senha deve ter no minimo 8 digitos tente novamente:",)
    if tem_maiuscula == False:
        print("A senha deve ter pelo menos 1 caractere Maiusculo.",)
    if tem_num ==False:
        print('A senha deve tem pelo menos 1 numero.')