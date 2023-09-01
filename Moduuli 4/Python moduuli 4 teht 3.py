p = int(-1)
s = int(1)
numero = int(0)
syöte = '0'

while syöte!='':
    syöte = (input('Anna luku: '))
    if syöte!='':
        numero = int(syöte)
        if numero > s:
            s = numero
        elif numero == -1 or numero < p:
            p = numero
print('Suurin numero on ' + str(s) + ' Pienin numero on ' + str(p))