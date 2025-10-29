class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros

    def kerros_ylos(self):
        self.kerros += 1
        print(f"Olet kerroksessa: {self.kerros}")

    def kerros_alas(self):
        self.kerros -= 1
        print(f"Olet kerroksessa: {self.kerros}")

    def siirry_kerrokseen(self, kerros):
        if kerros < self.alin_kerros or kerros > self.ylin_kerros:
            print(f"Kerrosta {kerros} ei ole")
            return
        while self.kerros < kerros:
            self.kerros_ylos()
        while self.kerros > kerros:
            self.kerros_alas()

    def siirry_alimpaan(self):
        if self.kerros != self.alin_kerros:
            self.siirry_kerrokseen(self.alin_kerros)


