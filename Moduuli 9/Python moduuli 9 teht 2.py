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

auto1 = Auto('ABC-123', 142)

auto1.kiihdytys(30)
auto1.kiihdytys(70)
auto1.kiihdytys(50)

print(f'Auton nopeus on {auto1.hetkellinen_nopeus} km/h.')

auto1.kiihdytys(-200)

print(f'Auto teki hätäjarrutuksen. sen nykyinen nopeus on {auto1.hetkellinen_nopeus}.')