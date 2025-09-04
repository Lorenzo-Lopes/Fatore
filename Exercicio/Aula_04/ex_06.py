#Peça para o usuário digitar a senha correta até que ele acerte.
import getpass

senha = "1234"

senha_digitada = getpass.getpass("Digite sua senha: ")

while senha_digitada != "1234":
    print ("Senha errada")
    senha_digitada = getpass.getpass("Digite sua senha: ")

print("Acesso liberado")
