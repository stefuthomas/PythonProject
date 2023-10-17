import random
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.hetkellinen_nopeus = 0
        self.kuljettu_matka = 0

autolista = []

numero = 0
for i in range(10):
    numero += 1
    rekisteritunnus = (f"ABC-{numero}")
    huippunopeus = random.randint(100, 200)
    auto = Auto(rekisteritunnus, huippunopeus)
    autolista.append(auto)

for auto in autolista:
    print(f"Rekisteritunnus: {auto.rekisteritunnus} ja huippunopeus: {auto.huippunopeus} km/h.")