luku_lista = []

luku = str(input('Syötä luku, tai lopeta painamalla "enter": '))
while luku!='':
    luku_lista.append(luku)
    luku = str(input('Syötä luku, tai lopeta painamalla "enter": '))

print("Pienin syötetty luku =",min(luku_lista))
print("Suurin syötetty luku =",max(luku_lista))