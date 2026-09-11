cp = 0

while cp < 3:
    print(f'Produto {cp}')
    cp = cp + 1

#While decrescente
i = 4

while i >= 0:
    print(i)
    i -= 1

#Repetição com entrada de usuario
jogar = 'sim'

while jogar.lower() == 'sim':
    print('repete ou inicia o jogo')
    jogar = input('Deseja jogar novamante: ')
    if jogar.lower() == 'nao':
        print('sair do jogo')
        break

#Modificadores de laco braker - continue
i = 0

while i < 10:
    i += 1

    if i == 3:
        continue

    print(f'Produto {i}')

# Modificadores de laco braker - break
i = 0

while i < 10:
    i += 1

    if i == 3 or i ==5:
        continue

    if i == 7:
        break

    print(f'Produto {i}')

#for
for cp in range(3):
    print(f'produto {cp}')

#de 1 ate 10, pulando de 2 em 2
for i in range(1, 11, 2):
    print(i)


#estrutura de repetição encadeada
for i in range(0, 4):
    for j in range(0, 3, 2):
        print(f'i:{i}, j:{j}')