# lambda - skrócony zapis funkcji
# lambda zawsze zwraca wynik
# funkcja anonimowa - mie ma nazwy, wykonanie w miejscu deklaracji
def oblicz_rabat(cena, procent):
    return cena * procent / 100


print(oblicz_rabat(500, 20))  # 100.0

oblicz_vat_lambda = lambda cena, procent: cena * procent / 100
print(oblicz_vat_lambda(500, 200))  # 1000.0

# lambda jako funkcja anonimowa
wynik = (lambda cena, rabat: cena - cena * rabat)(200, 0.15)
print(wynik)  # 170.0

# mapowanie
ceny_netto = [100, 250, 80, 1200, 45]

# list comprehensions
ceny_brutto = [round(cena * 1.23, 2) for cena in ceny_netto]
print(ceny_brutto)  # [123.0, 307.5, 98.4, 1476.0, 55.35]


def dodaj_vat(cena):
    return round(cena * 1.23, 2)


for cena in ceny_netto:
    ceny_brutto.append(dodaj_vat(cena))

# [123.0, 307.5, 98.4, 1476.0, 55.35, 123.0, 307.5, 98.4, 1476.0, 55.35]
print(ceny_brutto)

# funkcje wyższego rzędu
# funkcje które przyjmująjako argument inną funkcję
# lazy
ceny_brutto_map = list(map(dodaj_vat, ceny_netto))
print(ceny_brutto_map)  # [123.0, 307.5, 98.4, 1476.0, 55.35]

# lambda jako funkcja anonimowa
print(f"Lambda: {list(map(lambda cena: round(cena * 1.23, 2), ceny_netto))}")
# Lambda: [123.0, 307.5, 98.4, 1476.0, 55.35]

print(f"Lambda: {map(lambda cena: round(cena * 1.23, 2), ceny_netto)}")  # Lambda: <map object at 0x000001D49D777B80>

# filtrowanie
temperatury = [-12, -2, 0, 4, 15, 22, 31, 38, 38]

# wyfiltrowac do nowej listy, większe niż 30
upalne_dni = []

for t in temperatury:
    if t >= 30:
        upalne_dni.append(t)

print(upalne_dni)  # [31, 38, 38]

upalne_dni_2 = [temp for temp in temperatury if temp > 30]
print(upalne_dni_2)  # [31, 38, 38]

liczby = [1, 2, 3, 4, 5]

wynik = ["parzysta" if liczba % 2 == 0 else "nieparzysta" for liczba in liczby]
print(wynik)  # ['nieparzysta', 'parzysta', 'nieparzysta', 'parzysta', 'nieparzysta']

# filter()
upalne_dni_3 = list(
    filter(lambda t: t >= 30, temperatury)
)

print(upalne_dni_3)  # [31, 38, 38]

# > 10 , < 25
umiarkowane = list(
    # filter(lambda t: t > 10 and t < 25, temperatury)
    filter(lambda t: 10 < t < 25, temperatury)
)
print(umiarkowane)  # [15, 22]
# ctrl alt l

# wybrac ceny wieksze niz 100, obnizyc o 10%

ceny = [150, 250, 80, 75]

wiekszy_100 = list(
    filter(lambda cena: cena > 100, ceny)
)
print(wiekszy_100) # [150, 250]


