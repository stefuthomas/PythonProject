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
    def kulje(self, aika):
        uusi_matka = aika * 60
        self.kuljettu_matka = self.kuljettu_matka + uusi_matka


auto1 = Auto('ABC-123', 142)

auto1.kulje(1.5)

print(f'Auto kulki {1.5}h vauhdilla 60 km/h. Sen nykyinen kuljettu matka on {auto1.kuljettu_matka:.0f} kilometriä.')