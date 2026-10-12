cena = float(input("podaj cene:"))
znizka = float(input("podaj znizke w %:"))
cena_po_znizce = cena * (znizka/100)
cena_koncowa = round(cena_po_znizce,2)
roznica_1 = cena - cena_koncowa
roznica_2 = round(roznica_1,2)
print(f"cena poczatkowa: {cena}, znizka: {znizka}, po przecenie: {cena_koncowa}, roznica: {roznica_2}")