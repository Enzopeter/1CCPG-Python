#Logica E (AND)
#So vai logar quando o email e a senha forem verdadeiro

verifica_email = True
verifica_senha = False

login = verifica_email and verifica_senha
print(login)

if login:
    print('Entrar no programa')

#logica OU (OR)
#Quando 1 for verdadeiro todos os outros tambem são

logica_ou = False or False or True
print(logica_ou)

#Logica NEGAÇÃO (NOT)
#Inverte os valores

negação = not False
print(negação)

if not login:
    print('Loga certo ai...')


#Desafio de voto opicional
