#Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa
#paluuarvonaan vastaavan litramäärän.
#Halutaan -> Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
#Muunnos on tehtävä aliohjelmaa hyödyntäen.
#Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
#!Yksi gallona on 3,785 litraa!.


def muuntaja(gal):
    gallona = float(3.785)
    bensa = gal * gallona
    print(f'Määrä bensan lirtoina: {bensa:.2f} ')
    return

maara = float(input('Anna gallona määrä: '))
while maara>0:
    muuntaja(maara)
    maara = float(input('Anna gallona määrä: '))
print('Syötit negatiivisen arvon!')