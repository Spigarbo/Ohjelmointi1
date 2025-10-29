from .hissi import Hissi

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_maara):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = []
        for i in range(hissien_maara):
            self.hissit.append(Hissi(self.alin_kerros, self.ylin_kerros))
    def aja_hissia(self, hissin_numero, kohdekerros):
        print(f"Hissi numero {hissin_numero} liikkuu")
        self.hissit[hissin_numero - 1].siirry_kerrokseen(kohdekerros)

    def palohalytys(self):
        for hissi in self.hissit:
            hissi.siirry_alimpaan()
