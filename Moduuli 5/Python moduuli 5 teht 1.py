import random

heitot = int(input('Anna heittojen määrä: '))
summa = 0

for kerta in range(1,heitot + 1):
    sluku = random.randint(1,6)
    summa = sluku + summa
    print(f'heiton {kerta} silmäluku on {sluku}')

print(f'Silmälukujen summa on {summa}')