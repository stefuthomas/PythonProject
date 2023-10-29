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
        self.kuljettu_matka += self.hetkellinen_nopeus * tunnit
        print(f"{self.rekisteritunnus} kulki {tunnit} tuntia nopeudella {self.hetkellinen_nopeus} km/h."
              f"Se on nyt kulkenut {self.kuljettu_matka} km.")

class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekisteritunnus, huippunopeus)

    def kulje(self, tunnit):
        print("Sähköauto:")
        super().kulje(tunnit)

    def kiihdytys(self, muutos):
        super().kiihdytys(muutos)

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki_koko):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.bensatankki_koko = bensatankki_koko
        super().__init__(rekisteritunnus, huippunopeus)

    def kulje(self, tunnit):
        print("Polttomoottoriauto:")
        super().kulje(tunnit)

    def kiihdytys(self, muutos):
        super().kiihdytys(muutos)


sauto = Sahkoauto("ABC-15", 180, 52.5)
pauto = Polttomoottoriauto("ABC-123", 165, 32.3)

sauto.kiihdytys(200)
pauto.kiihdytys(145)

sauto.kulje(3)
pauto.kulje(3)