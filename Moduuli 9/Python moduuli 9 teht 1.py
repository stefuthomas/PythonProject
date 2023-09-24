class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.hetkellinen_nopeus = 0
        self.kuljettu_matka = 0

auto1 = Auto('ABC-123', 142)

print('Auton tiedot:')
print(f'Auton rekisteritunnus: {auto1.rekisteritunnus}')
print(f'Auton huippunopeus: {auto1.huippunopeus}km/h')
print(f'Auton hetkellinen nopeus: {auto1.hetkellinen_nopeus}km/h')
print(f'Auton kuljettu matka: {auto1.kuljettu_matka}km')