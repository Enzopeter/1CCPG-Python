print("ola mundo")
print(11+4)
print('1' + '2') #juntando

#Variáveis
nome = 'enzo' #string
idade = 26 #int
peso = 70.7 #float

print('oiii \n', nome, idade, peso)
print(f'ola,{nome}')

#input, recebe informações
nome = input('Qual o seu nome?: ')
idade = int(input('Qual a sua idade?: '))
peso = float(input('Qual o seu peso?: '))

print(nome, idade, peso)
print(idade + 1)

ano_nascimento = 1999
ano_atual = 2026
idade = ano_atual - ano_nascimento
print(f'sua idade é: {idade}')