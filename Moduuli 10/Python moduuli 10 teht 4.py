import random
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.hetkellinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytys(self, muutos):
        uusi_nopeus = self.hetkellinen_nopeus + muutos
        if uusi_nopeus > self.huippunopeus:
            self.hetkellinen_nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.hetkellinen_nopeus = 0
        else:
            self.hetkellinen_nopeus = uusi_nopeus

    def kulje(self,tunnit):
        self.kuljettu_matka += self.hetkellinen_nopeus * tunnit

class Kilpailu:

    tunti = 0
    def __init__(self, kilpailun_nimi, kilpailun_pituus):
        self.kilpailun_nimi = kilpailun_nimi
        self.kilpailun_pituus = kilpailun_pituus
        self.osallistuvat_autot = self.auto_luonti()

    def auto_luonti(self):
        autolista = []
        for i in range(1, 11):
            auto = Auto(f"ABC-{i}", random.randint(100, 200))
            autolista.append(auto)
        return autolista

    def tunti_kuluu(self):
        kilpailu.tunti = kilpailu.tunti + 1
        for auto in kilpailu.osallistuvat_autot:
            auto.kiihdytys(random.randint(-10, 15))
            auto.kulje(1)
        if kilpailu.tunti == 10:
            kilpailu.tunti = 0
            kilpailu.tulosta_tilanne()

    def tulosta_tilanne(self):
        print("\nKilpailun tilanne:\n")
        for auto in kilpailu.osallistuvat_autot:
            print(f"Auto {auto.rekisteritunnus} nopeus: {auto.hetkellinen_nopeus} km/h"
                  f" kuljettu matka: {auto.kuljettu_matka} kilometriä.")

    def kilpailu_ohi(self):
        for auto in kilpailu.osallistuvat_autot:
            if auto.kuljettu_matka >= kilpailu.kilpailun_pituus:
                return True
        return False

kilpailu = Kilpailu("Suuri romuralli", 8000)

gameRunning = kilpailu.kilpailu_ohi()

while gameRunning != True:
    kilpailu.tunti_kuluu()
    for auto in kilpailu.osallistuvat_autot:
        gameRunning = kilpailu.kilpailu_ohi()

kilpailu.tulosta_tilanne()

for auto in kilpailu.osallistuvat_autot:
    if auto.kuljettu_matka >= kilpailu.kilpailun_pituus:
        print(f"Voittaja: {auto.rekisteritunnus}")