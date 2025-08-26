sukupuoli = input("Mikä on biologinen sukupuolesi, Nainen vai Mies? ")
hemhob_arvo = float(input("Syötä hemoglobiiniarvosi:"))

if sukupuoli == "Nainen" and 117 <= hemhob_arvo <= 175:
    print("Hemoglobiiniarvo on normaali")
if sukupuoli == "Nainen" and hemhob_arvo > 175:
    print("Hemoglobiiniarvo on liian korkea")
if sukupuoli == "Nainen" and hemhob_arvo < 117:
    print("Hemoglobiiniarvo on liian matala")

if sukupuoli == "Mies" and 134 <= hemhob_arvo <= 195:
    print("Hemoglobiiniarvo on normaali")
if sukupuoli == "Mies" and hemhob_arvo > 195:
    print("Hemoglobiiniarvo on liian korkea")
if sukupuoli == "Mies" and hemhob_arvo < 134:
    print("Hemoglobiiniarvo on liian matala")

