class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def siirry_kerrokseen(self, kohde):
        if self.nykyinen_kerros < kohde:
            while self.nykyinen_kerros != kohde:
                self.kerros_ylös()

        elif self.nykyinen_kerros > kohde:
            if self.nykyinen_kerros > kohde:
                while self.nykyinen_kerros != kohde:
                    self.kerros_alas()

        elif kohde == self.ylin_kerros:
            self.nykyinen_kerros = self.ylin_kerros

        elif kohde == self.alin_kerros:
            self.nykyinen_kerros = self.alin_kerros

        print(f"Olet nyt kerroksessa: {self.nykyinen_kerros}")


    def kerros_ylös(self):
        self.nykyinen_kerros = self.nykyinen_kerros + 1

    def kerros_alas(self):
        self.nykyinen_kerros = self.nykyinen_kerros - 1

h = Hissi(1, 10)

h.siirry_kerrokseen(5)
h.siirry_kerrokseen(8)
h.siirry_kerrokseen(1)