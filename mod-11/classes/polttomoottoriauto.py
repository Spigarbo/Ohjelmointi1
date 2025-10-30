from .uusiauto import Auto
class Polttomoottoriauto(Auto):
    def __init__(self, new_rekisteritunnus, new_huippunopeus, litrat):
        super().__init__(new_rekisteritunnus, new_huippunopeus)
        self.litrat = litrat