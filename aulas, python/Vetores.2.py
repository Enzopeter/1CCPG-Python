lista_frutas = ["Banana", "Maçã", "Morango"]

print(lista_frutas[0])  #Banana
print(lista_frutas[1])  #Maçã
print(lista_frutas[2])  #Morango
print()

print(lista_frutas[1:3]) #Ve apenas os valores até o 2, Banana e Maçã
print()

lista_frutas.append("Pera") #Adiciona a "Pera" no final da lista
print(lista_frutas)
print()

qtd_frutas = len(lista_frutas)
print("Quantidade de frutas", qtd_frutas)
print()

#For Indexado
for i in range(qtd_frutas):
    print(lista_frutas[i])  #Percorre as posições/numeros da lista

print()

#For EACH no python
for fruta in lista_frutas:
    print(fruta)  #Percorre o elemento da lista

print()


numeros = [0, 5, 11, 4]
for numero in numeros:
    print(numero)

print()


#ATIVIDADE
pessoas = ["Enzo", "Ana", "João", "José"]
for i in range(len(pessoas)):
    for j in range (i + 1, len(pessoas)):
        print(pessoas[i], pessoas[j])