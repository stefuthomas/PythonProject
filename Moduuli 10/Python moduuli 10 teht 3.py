class Hissi:
    def __init__(self, numero, akerros, ykerros):
        self.numero = numero
        self.akerros = akerros
        self.ykerros = ykerros
        self.nkerros = akerros

    def siirry_kerrokseen(self, kohde):
        if self.nkerros < kohde:
            while self.nkerros != kohde:
                self.kerros_ylös()

        elif self.nkerros > kohde:
            if self.nkerros > kohde:
                while self.nkerros != kohde:
                    self.kerros_alas()

        elif kohde == self.ykerros:
            self.nkerros = self.ykerros

        elif kohde == self.akerros:
            self.nkerros = self.akerros

        print(f"Olet nyt hissillä {self.numero} kerroksessa {self.nkerros}")


    def kerros_ylös(self):
        self.nkerros = self.nkerros + 1

    def kerros_alas(self):
        self.nkerros = self.nkerros - 1

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_määrä):
        self.alin_kerros = int(alin_kerros)
        self.ylin_kerros = int(ylin_kerros)
        self.hissien_määrä = int(hissien_määrä)
        self.hissit = self.hissienLuonti()
    def hissienLuonti(self):
        hissilista = []
        for i in range(self.hissien_määrä):
            hissi = Hissi(i+1, self.alin_kerros, self.ylin_kerros)
            hissilista.append(hissi)
        return hissilista
    def aja_hissiä(self, hissin_numero, kohde_kerros):
        hissi = talo.hissit[hissin_numero-1]
        hissi.siirry_kerrokseen(kohde_kerros)
    def palohälytys(self):
        print("Palohälytys!")
        for hissi in talo.hissit:
            hissi.nkerros = hissi.akerros
            print(f"Hissi {hissi.numero} on kerroksessa {hissi.nkerros}")

talo = Talo(1, 10,2)
talo.aja_hissiä(1,6)
talo.aja_hissiä(2,4)
talo.palohälytys()