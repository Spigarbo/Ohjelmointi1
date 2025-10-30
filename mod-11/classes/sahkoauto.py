from .uusiauto import Auto

class Sahkoauto(Auto):
    def __init__(self, new_rekisteritunnus, new_huippunopeus, kapasiteetti):
        super().__init__(new_rekisteritunnus, new_huippunopeus)
        self.kapasiteetti = kapasiteetti
