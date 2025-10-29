luvut = []

tulostetut_luvut = []

arvo_str = input("Anna luku, tyhjä lopettaa: ")

while arvo_str != "":
    arvo = int(arvo_str)
    luvut.append(arvo)
    arvo_str = input("Anna luku, tyhjä lopettaa: ")

for luku in luvut:
    if luku not in tulostetut_luvut and luku > 100:
        print(luku)
        tulostetut_luvut.append(luku)
