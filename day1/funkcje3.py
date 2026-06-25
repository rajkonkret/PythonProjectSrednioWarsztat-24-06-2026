# lambda - skrócony zapis funkcji
# lambda zawsze zwraca wynik
# funkcja anonimowa - mie ma nazwy, wykonanie w miejscu deklaracji
from functools import reduce, lru_cache


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
print(wiekszy_100)  # [150, 250]

rabat_100 = list(
    map(lambda cena: cena * 0.9, wiekszy_100)
)

print(list(map(lambda cena: cena * 0.9, filter(lambda cena: cena > 100, ceny))))  # [135.0, 225.0]

print(rabat_100)  # [135.0, 225.0]

# max()
najwieksza = max(ceny)
print(najwieksza)  # 250

pracownicy = [
    {'imie': "Anna", "pensja": 7500, "wiek": 33},
    {'imie': "Radek", "pensja": 17500, "wiek": 41},
    {'imie': "Tomek", "pensja": 6500, "wiek": 29},
    {'imie': "Marek", "pensja": 12000, "wiek": 35},
]

najlepiej_oplacony = max(
    pracownicy,
    key=lambda osoba: osoba['pensja']
)

print(najlepiej_oplacony)  # {'imie': 'Radek', 'pensja': 17500, 'wiek': 41}

# min()
najmlodszy = min(
    pracownicy,
    key=lambda osoba: osoba['wiek']
)

print(najmlodszy)  # {'imie': 'Tomek', 'pensja': 6500, 'wiek': 29}
# any(), all()

# sorted()
posortowani = sorted(
    pracownicy,
    key=lambda osoba: osoba['wiek']
)

print(posortowani)

r0 = {'miasto': "Kielce"}
r1 = {'miasto': "Kielce", "ZIP": "25-900"}

d_zip = lambda row: row.setdefault("ZIP", "00-000")
print(d_zip(r0))
print(d_zip(r1))

print(r0)  # {'miasto': 'Kielce', 'ZIP': '00-000'}

# reduce()
#  reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5)
liczby = [1, 3, 4, 5]
wynik = reduce(lambda x, y: x * y, liczby)
print(wynik)  # 60

# reduce(lambda x,y: x + y, []) # TypeError: reduce() of empty iterable with no initial value
print(reduce(lambda x, y: x + y, [], 0))  # 0


# lru_cache()

@lru_cache(maxsize=100)
def oblicz_koszt_wysylki(kraj, waga):
    print(f"Obliczam koszt dla: {kraj}, {waga} kg")

    ceny_bazowe = {
        "Polska": 15,
        "Niemcy": 35,
        "Francja": 45,
    }

    cena_bazowa = ceny_bazowe.get(kraj, 70)

    return cena_bazowa + waga * 2


print(oblicz_koszt_wysylki("Polska", 5))
# Obliczam koszt dla: Polska, 5 kg
# 25
print(oblicz_koszt_wysylki("Polska", 5))
# 25  - wyciagnięte z cache

print(oblicz_koszt_wysylki.cache_info())
# CacheInfo(hits=1, misses=1, maxsize=100, currsize=1)

oblicz_koszt_wysylki.cache_clear()
print(oblicz_koszt_wysylki.cache_info())
# CacheInfo(hits=0, misses=0, maxsize=100, currsize=0)
