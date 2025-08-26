fysiikan_arvosana = int(input("Anna fysiikan arvosanasi: "))
matematiikan_arvosana = int(input("Anna matematiikan arvosanasi: "))
kemian_arvosana = int(input("Anna kemian arvosanasi: "))

if fysiikan_arvosana < 50 or matematiikan_arvosana < 50 or kemian_arvosana < 50:
    print("Ikävä kyllä et saanut stipendiä tällä kertaa")
elif fysiikan_arvosana > 90 and matematiikan_arvosana > 90:
    print("Onneksi olkoon, sait stipendin")
elif kemian_arvosana > 95:
    print("Onneksi olkoon, sait stipendin")
else:
    print("Ikävä kyllä et saanut stipendiä tällä kertaa")