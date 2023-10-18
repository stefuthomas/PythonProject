class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alinkerros = alin_kerros
        self.ylinkerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def siirry_kerrokseen(self, kohde):
        if self.nykyinen_kerros < kohde:
            while self.nykyinen_kerros != kohde:
                h.kerros_ylös()

        elif self.nykyinen_kerros > kohde:
            if self.nykyinen_kerros > kohde:
                while self.nykyinen_kerros != kohde:
                    h.kerros_alas()

        elif kohde == self.ylinkerros:
            self.nykyinen_kerros = self.ylinkerros

        elif kohde == self.alinkerros:
            self.nykyinen_kerros = self.alinkerros

        print(f"Olet nyt kerroksessa: {self.nykyinen_kerros}")


    def kerros_ylös(self):
        self.nykyinen_kerros = self.nykyinen_kerros + 1

    def kerros_alas(self):
        self.nykyinen_kerros = self.nykyinen_kerros - 1

h = Hissi(1, 10)

h.siirry_kerrokseen(5)
h.siirry_kerrokseen(8)
h.siirry_kerrokseen(1)