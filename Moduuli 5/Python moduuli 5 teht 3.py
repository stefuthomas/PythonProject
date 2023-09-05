#Alkuluku on luku, joka on jaollinen 1 ja itsellään kuten 13.
#Luku 21 ei ole alkuluku. Se on jaollinen luvuilla 1 ja itsellään, mutta myös 3 ja 7.

#Step 1 -> Kysy lukuja
#Step 2 -> Kokeile onko luku jaollinen VAIN itsellään ja 1

def alkuluku(numero):
    for i in range(2, numero - 1, 1):
        if numero % i == 0:
            numero = True
            break
    if numero != True:
        print('Luku on alkuluku.')
    else:
        print('Luku ei ole alkuluku')
    return

luku = int(input('Anna luku: '))
if luku < 2:
    print('Luku ei ole alkuluku')
else:
    alkuluku(luku)