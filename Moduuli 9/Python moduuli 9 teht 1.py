class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.hetkellinen_nopeus = 0
        self.kuljettu_matka = 0

    def tiedot(self):
        print('Auton tiedot:')
        print(f'Auton rekisteritunnus: {self.rekisteritunnus}')
        print(f'Auton huippunopeus: {self.huippunopeus}km/h')
        print(f'Auton hetkellinen nopeus: {self.hetkellinen_nopeus}km/h')
        print(f'Auton kuljettu matka: {self.kuljettu_matka}km')

auto1 = Auto('ABC-123',142)
auto1.tiedot()