#Função sem retorno e sem paremetro
def print_lyrics():
    print("i ain't gonna live forever")
    print("i just want to live while i'm alive")

print_lyrics()
print_lyrics()


#Função sem retorno com parametro
def boas_vindas(nome):
    print(f'Olá {nome}!! Seja bem-vindo')

nome_digitado = input('Digite seu nome:  ')
boas_vindas(nome_digitado)

#Função sem retorno e sem parametro
def soma(num_a, num_b):
    soma = num_a + num_b
    return soma

print(soma(10,5))
print(type(nome_digitado))