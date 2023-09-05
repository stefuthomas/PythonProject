import math

def yksikkohinta(halkaisija, euro):
    pinta_ala = math.pi * (halkaisija / 2) ** 2 / 10000
    arvo = pinta_ala / euro
    print(f'Pizzan yksikköhinta euroissa on: {arvo}')
    return arvo

pizza1 = float(input('Anna ensimmäisen pizzan halkaisija: '))
hinta1 = float(input('Anna ensimmäisen pizzan hinta euroissa: '))
pizza2 = float(input('Anna toisen pizzan halkaisija: '))
hinta2 = float(input('Anna toisen pizzan hinta euroissa: '))

yksikkohinta1 = yksikkohinta(pizza1, hinta1)
yksikkohinta2 =  yksikkohinta(pizza2, hinta2)

if yksikkohinta2 < yksikkohinta1:
    print('Ensimmäinen pizza on parempi hinnaltaan.')
elif yksikkohinta1 < yksikkohinta2:
    print('Toinen pizza on parempi hinnaltaan.')
else:
    print('Molemmat pizzat ovat hinnaltaan yhtä hyviä.')