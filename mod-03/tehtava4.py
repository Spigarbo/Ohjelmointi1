vuosi = int(input("Mikä vuosi? "))

vuosi1 = float(vuosi / 4)
vuosi2 = float(vuosi / 400)
if vuosi1.is_integer() and vuosi2.is_integer():
    print("Vuosi on karkausvuosi")
else:
    print("Vuosi ei ole karkausvuosi")