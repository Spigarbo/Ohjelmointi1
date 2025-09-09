def karsija(lista):
    karsittu_lista = []
    for i in lista:
        if i % 2 == 0:
            karsittu_lista.append(i)
    return karsittu_lista

lista = []
luku = input("Syötä jokin kokonaisluku, enter lopettaa: ")
while luku != "":
    lista.append(int(luku))
    luku = input("Syötä jokin kokonaisluku, enter lopettaa: ")
karsittu_lista = karsija(lista)
print(f"Tässä lista jossa vain parilliset luvut: {karsittu_lista}")
print(f"Tässä lista jossa kaikki luvut: {lista}")