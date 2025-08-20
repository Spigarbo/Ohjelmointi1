import math

suorakulmion_kanta = input("Syötä suorakulmion kanta: ")
suorakulmion_korkeus = input("Syötä suorakulmion korkeus: ")

suorakulmion_ala = float(suorakulmion_korkeus) * float(suorakulmion_kanta)
suorakulmion_piiri = float(suorakulmion_kanta) * 2 + float(suorakulmion_korkeus) * 2

print("Suorakulmion ala on: ")
print(suorakulmion_ala)
print("Suorakulmion piiri on: ")
print(suorakulmion_piiri)