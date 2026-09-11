salas = [
        [28, 31, 34, 33 ],
        [25, 27, 29, 28 ],
        [32, 35, 36, 34 ],
        [24, 26, 25, 27 ],
]

lista_crit = []

for sala in salas:
    print(sala)

    soma = 0

    qtd = 0

    for temperatura in sala:
        print(temperatura)
        soma += temperatura

        if temperatura >= 33:
            qtd += 1

    lista_crit.append(qtd)
    print(f'Quantidae de criticos registrados {qtd}')

    media = soma / len(sala)
    print(f'A Media Das Temperaturas Da Sala Foi: {media}')

mais_crits = max(lista_crit)
sala_crit = lista_crit.index(mais_crits)
print(f'A Sala Com O Maior Critico Foi A: {sala_crit + 1}')


