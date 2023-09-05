#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
#Ohjelma palauttaa listassa olevien lukujen summan.
#Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

lista = [0, 5, 10, 15, 20, 25, 30]

def laskuri(numerot):
    summa = 0
    for i in numerot:
        summa = i + summa
    print(summa)
    return
print(f'Luvut listassa ovat: {lista}')
print('Listan lukujen summa: ')
laskuri(lista)
