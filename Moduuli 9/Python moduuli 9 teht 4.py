import random
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.hetkellinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytys(self, muutos):
        uusi_nopeus = self.hetkellinen_nopeus + muutos
        if uusi_nopeus < 0:
            self.hetkellinen_nopeus = 0
        elif uusi_nopeus > self.huippunopeus:
            self.hetkellinen_nopeus = self.huippunopeus
        else:
            self.hetkellinen_nopeus = uusi_nopeus

    def kulje(self,):
        kuljettuMatka = 1 * self.hetkellinen_nopeus
        self.kuljettu_matka = kuljettuMatka + self.kuljettu_matka

def tulokset(autolista):
    if any(auto.kuljettu_matka >= 10000 for auto in autolista):
        return False
    else:
        return True


autolista = []


for i in range(1, 11):
    rekisteritunnus = (f"ABC-{i}")
    huippunopeus = random.randint(100, 200)
    auto = Auto(rekisteritunnus, huippunopeus)
    autolista.append(auto)

print("Autojen tiedot:")

for auto in autolista:
    print(f"Rekisteritunnus: {auto.rekisteritunnus}. Huippunopeus: {auto.huippunopeus} km/h.")

print("")

gameRunning = True

while gameRunning:

    for auto in autolista:
        auto.kiihdytys(random.randint(-10, 15))

    for auto in autolista:
        auto.kulje()

    for auto in autolista:
        gameRunning = tulokset(autolista)

for auto in autolista:
    print(f"Rekisteritunnus: {auto.rekisteritunnus}. Huippunopeus: {auto.huippunopeus} km/h. "
          f"Nopeus: {auto.hetkellinen_nopeus} ja kuljettu matka: {auto.kuljettu_matka}.")