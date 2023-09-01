import random

kokonaisluku = random.randint(1,10)
arvaus = int(input('Anna arvauksesi: '))

while arvaus!=kokonaisluku:
    if arvaus > kokonaisluku:
        print('Arvauksesi on suurempi kuin luku.')
        arvaus = int(input('Anna arvaus: '))
    if arvaus < kokonaisluku:
        print('Arvauksesi on pienempi kuin luku.')
        arvaus = int(input('Anna arvaus: '))

print('Oikein arvattu')