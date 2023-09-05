#Alkuluku on luku, joka on jaollinen 1 ja itsellään kuten 13.
#Luku 21 ei ole alkuluku. Se on jaollinen luvuilla 1 ja itsellään, mutta myös 3 ja 7.

#Step 1 -> Kysy lukuja
#Step 2 -> Kokeile onko luku jaollinen VAIN itsellään ja 1

luku = int(input('Syötä kokonaisluku: '))
isAlku = True

if luku < 1:
    print('Luku ei ole alkuluku.')

for i in range(luku):
    if luku % luku ==0 and luku!=0:
        isAlku = True
        break
    elif luku % luku == 0 and luku % i ==0:
        break
i = i + 1
if isAlku == True:
    print ('Luku on alkuluku.')
elif isAlku == False:
    print('Luku ei ole alkuluku.')