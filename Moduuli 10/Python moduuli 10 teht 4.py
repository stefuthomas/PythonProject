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

    def kulje(self, tunnit):
        uusi_kuljettu_matka = self.kuljettu_matka + tunnit * self.hetkellinen_nopeus
        self.kuljettu_matka = uusi_kuljettu_matka

class Kilpailu:
    def __init__(self, kilpaiun_nimi, kilpailun_pituus):
        self.kilpailun_nimi = kilpaiun_nimi
        self.kilpailun_pituus = kilpailun_pituus
        self.osallistuvat_autot = self.auto_luonti()

    def auto_luonti(self):
        autolista = []
        for i in range(1, 11):
            auto = Auto(f"ABC-{i}", random.randint(100, 200))
            autolista.append(auto)
        return autolista
    def tunti_kuluu(self):
        for auto in kilpailu.osallistuvat_autot:
            auto.kiihdytys(random.randint(-10,15))
            auto.kulje(1)

    def tulosta_tilanne(self):
        for auto in kilpailu.osallistuvat_autot:
            print(f"Auton {auto.rekisteritunnus} nopeus on {auto.hetkellinen_nopeus} km/h."
                  f"Auton {auto.rekisteritunnus} kuljettu matka on nyt {auto.kuljettu_matka} kilometriä.")

kilpailu = Kilpailu("Suuri rmuralli", 8000)
