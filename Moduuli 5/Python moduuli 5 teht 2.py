lista = []
luku = input('Anna lukuja tai lopeta painamalla "enter": ')
while luku!='':
    lista.append(int(luku))
    luku = input('Anna lukuja tai lopeta painamalla "enter": ')

lista.sort(reverse=True)

for i in range(5):
    print(f'Syötettyjen lukujen viisi suurinta järjestyksessä {lista[i]}')