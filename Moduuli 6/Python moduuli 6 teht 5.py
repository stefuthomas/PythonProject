lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def laskuri(numerot):
    jaolliset_numerot = []
    for n in numerot:
        if n % 2==0:
            jaolliset_numerot.append(n)
    print(jaolliset_numerot)
    return

print(f'Luvut listassa ovat: {lista}')
print('Listan parilliset luvut: ')
laskuri(lista)