#Loja digital

print('Olá, seja bem-vindo! a elotroeletronicos.')
Prod = input('Tenha algo que vc gostaria de compar, digite o nome do produto: ')
Valor = float(input('O valor do produto será de:'))

print(f'O valor do {Prod} é de {Valor} reais')
Qnt = int(input(f'quantos do produto {Prod} você gostaria? '))

Valor_Bruto = (Valor * Qnt)

Desconto = int(input('Quanto de desconto a pessoa receberá? de 10 até 20% '))

valor_Desconto = (Valor_Bruto * Desconto /100)

print(f'Parabens, você recebeu um desconto de {Desconto}%, o produto ficara {valor_Desconto} reais')

final = Valor_Bruto - valor_Desconto

print(f'O valor bruto da compra ficará {Valor_Bruto} reais, o valor do desconto fica {Desconto}% e o valor final da compra ficará em {final}')

#empresa
colaborador = input('Olá qual seu nome? ')
print(f'Olá seja bem vindo! {colaborador}')

horaTB = float(input('Quantas horas você trabalhou no mês ? '))
print(f'o colaborador {colaborador}, trabalhou {horaTB} horas no mês')

valorH = 5
ganho = horaTB * valorH
print(f'{colaborador} ganhou {ganho} no mês')

horaE = float(input('fez horas extras no mes ? '))
valor_total = horaE * valorH + ganho
print(f'Voce ganhou no total {valor_total}')

descontoV = float(input('o desconto do mes sera de?'))
Depois = valor_total - descontoV

print(f'O salario bruto é de {ganho} com as horas extras fica {valor_total} reais e depois apos os descontos ficara sobrando {Depois} reais')
