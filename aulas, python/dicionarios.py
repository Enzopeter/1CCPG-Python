eng2sp = dict()
print(eng2sp)

eng2sp['one'] = 'uno'
print(eng2sp)

eng2sp = {
    'one': 'uno',
    'two': 'dos',
    'three': 'tres'
}
print(eng2sp)
print(eng2sp['two']) #--> 'dos' não é uma chave é um valor

print('one' in eng2sp)

valores = eng2sp.values()
print('uno' in valores) #--> neste caso o 'one' não é valor é chave

print(eng2sp.items())
print()

def count_letters(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

dict_contagem = count_letters('aura e ego')
print(dict_contagem)


