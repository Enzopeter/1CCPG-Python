#Escolha do usuario
#0 ---> sair do programa
#1 ---> entra no programa
# ----> erro!

escolha_usuario = 0

match escolha_usuario:
    case 0:
        print('Sair do programa')
    case 1:
        print('Entrar no programa')
    case _:
        print('ERRO!!')