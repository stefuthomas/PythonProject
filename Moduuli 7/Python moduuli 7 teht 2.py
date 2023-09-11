nimet = set()

nimi = input('Anna nimi, tai lopeta painamalla "enter": ')

while nimi!='':
    if nimi in nimet:
        print('Aiemmin syötetty nimi.')
    else:
        print('Uusi nimi.')
    nimet.add(nimi)
    nimi = input('Anna nimi, tai lopeta painamalla "enter": ')

for i in nimet:
    print(i)