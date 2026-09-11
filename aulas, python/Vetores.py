#Criando lista de inteiros
vetor_inteiros = []
vetor_inteiros.append(10) #adiciona 10 na posição 0
vetor_inteiros.append(20) #adiciona 20 na posição 1

print(vetor_inteiros[0])

#lista com textos
texto = "FIAP Paulista"

tamanho_str = len(texto)
print(tamanho_str)

print(texto[0])
print(texto[1])
print(texto[2])
print(texto[3])

print()

for i in range(tamanho_str):
    print(i, texto[i])

for c in texto:
    print(c)

