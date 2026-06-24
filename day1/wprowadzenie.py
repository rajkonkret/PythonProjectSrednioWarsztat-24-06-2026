# https://peps.python.org/pep-0008/
# snake_case
import sys

print("")
print('')

# blake
print("pierwsza linia")
print('pierwsza linia')

# ctrl / - komentarz
# print("pierwsza linia')
#   File "C:\Users\CSComarch\PycharmProjects\PythonProject\day1\wprowadzenie.py", line 11
#     print("pierwsza linia')
#           ^
# SyntaxError: unterminated string literal (detected at line 11)
#
# Process finished with exit code 1

"""
komentarz
    wielolinijkowy (dokumentacja)"""

info = """
tekst
wielolinijkowy
    zachowuje
        formatowanie"""

print(info)
# "tekst
# wielolinijkowy
#     zachowuje
#         formatowanie"

# typowanie dynamiczne
print(type(info))  # <class 'str'>

# ctrl alt l - formatowanie
info = 90
print(type(info))  # <class 'int'> liczba całkowita

print(sys.int_info)
# sys.int_info(bits_per_digit=30, sizeof_digit=4,
# default_max_str_digits=4300, str_digits_check_threshold=640)

info = "Radek"
print(info)

print("12" + "45")  # konkatenacja -> 1245
print(12 * "40")  # 404040404040404040404040

# print("12" + 40)  # TypeError: can only concatenate str (not "int") to str
# silne typowanie - nie zmienia sam typów
# rzutowanie
print(int(12) + int("40"))  # 52

# float - liczba zmiennoprzecinkowa
print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308,
# min=2.2250738585072014e-308, min_exp=-1021,
# min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

# błąd zaokrąglenia
print(0.1 + 0.9)  # 1.0
print(0.1 + 0.2)  # 0.30000000000000004
# For example, in a floating-point arithmetic with five base-ten digits,
# the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345.

# decimal() - pozwala ominąć problem błędu zaokrąglenia

# boolean
# True, False
# 1, 0

print(bool(100))  # True
print(bool("radek"))  # True

print(bool(""))  # False
print(bool("0"))  # True

# kolekcje
# mogą przechowywwac wiele elemntów - róznego typu na raz

# lista - zachowuje kolejność przy dodawaniu elementów, mutowalna
imiona = ["Jan", "Piotr", "Anna", "Nadia", "Michał"]
print(imiona)
print(type(imiona))  # <class 'list'>

# ['Jan', 'Piotr', 'Anna', 'Nadia', 'Michał']
#   0       1         2        3        4
#   -5      -4        -3       -2         -1
print(imiona[1])  # Piotr
print(imiona[-1])  # Michał

print(imiona[-2])

# slicowanie - fragment listy
print(imiona[2:4])  # ['Anna', 'Nadia'] z prawej niewłącznie
print(imiona[1:])  # włacznie z ostatnim, ['Piotr', 'Anna', 'Nadia', 'Michał']

print(imiona[2:7])  # ['Anna', 'Nadia', 'Michał']

print(imiona[10:34])  # []
# imiona[10] # IndexError: list index out of range

print(imiona[-2:0])  # [3:0]
print(imiona[0:-2])  # [0:3] -> ['Jan', 'Piotr', 'Anna']

imiona_p = imiona[::2]  # [start:stop:krok]
print(imiona_p)  # ['Jan', 'Anna', 'Michał']

print(imiona[::-1])  # ['Michał', 'Nadia', 'Anna', 'Piotr', 'Jan']

# pusta lista
lista_p = list()
lista_p2 = []
print(lista_p2)  # []

lista_p.append("Karol")
lista_p.append("Radek")
lista_p.append("Tomek")
lista_p.append("Anna")
print(lista_p)  # ['Karol', 'Radek', 'Tomek', 'Anna']

lista_p.insert(1, "Jan")  # na wskazanym indeksie
print(lista_p)  # ['Karol', 'Jan', 'Radek', 'Tomek', 'Anna']

lista_p.append("Jan")

# usunięcie z listy, pierwszy napotkany
lista_p.remove("Jan")
print(lista_p)  # ['Karol', 'Radek', 'Tomek', 'Anna', 'Jan']

# pop() - usunięcie po indeksie
# usunie ostani, zwraca usuniety

# garbage collector

del imiona[3]
print(imiona)  # ['Jan', 'Piotr', 'Anna', 'Michał']

del lista_p2  # usunięcie listy
# print(lista_p2) # NameError: name 'lista_p2' is not defined. Did you mean: 'lista_p'?

nowe_imie = imiona
print(imiona)  # ['Jan', 'Piotr', 'Anna', 'Michał']
print(nowe_imie)  # ['Jan', 'Piotr', 'Anna', 'Michał']

print(id(imiona))  # 1601884180416
print(id(nowe_imie))  # 1601884180416

# kopia elementów listy
nowa_lista = imiona.copy()
print(id(nowa_lista))  # 2155757094592

imiona.clear()
print(imiona)  # []
print(nowe_imie)  # []

print(nowa_lista)  # ['Jan', 'Piotr', 'Anna', 'Michał']
nowa_lista.append("Radek")

nowe_imie.append("Radek")

print(nowe_imie)
print(nowa_lista)
print(imiona)
# ['Radek']
# ['Jan', 'Piotr', 'Anna', 'Michał', 'Radek']
# ['Radek']

pimie = imiona[:]
qimie = list(imiona)
print(id(pimie))
print(id(qimie))
print(id(imiona))
# 2047535348416
# 2047572868096
# 2047533174720

# tupla - krotka
# kolekcja niemutowalna
# tylko do odczyty
# pozwala lepiej zarzadzac pamięcią

miasto = "Kraków", "Lublin", "Płock", "Łódź"
# miasto = ("Kraków", "Lublin", "Płock", "Łódź")
print(type(miasto))  # <class 'tuple'>

krotka_jedn = ("radek",)  # pep8 tak zaleca
print(type(krotka_jedn))  # <class 'tuple'>

print(miasto.index("Łódź"))  # index numer 3
print(miasto.count("Łódź"))  # występuje 1 raz

# del miasto[0] # TypeError: 'tuple' object doesn't support item deletion

del miasto
# print(miasto)  # NameError: name 'miasto' is not defined

# zbiór, set
# nie przechowują duplikatów
# nie zachowuje kolejności (brak indeksu)
# hashowane

drzewa = {'jodłą', 'buk', "świerk", 'dąb', 'klon'}
print(drzewa)  # {'dąb', 'klon', 'świerk', 'jodłą', 'buk'}
print(type(drzewa))  # <class 'set'>

drzewa.add('osika')
drzewa.add('osika')
drzewa.add('osika')
drzewa.add('osika')
drzewa.add('osika')
print(drzewa)
# {'osika', 'świerk', 'klon', 'buk', 'jodłą', 'dąb'}

# pusty zbiór
pusty_zbior = set()  # tylko i wyłacznie za pomocą set()
print(pusty_zbior)  # set()

lista = [1, 2, 3, 4, 4, 7, 7, 6, 5, 1, 3, 4, 5, 6, 7, "A"]
zbior = set(lista)
print(zbior)  # {1, 2, 3, 4, 5, 6, 7, 'A'} bez zachowania kolejnosci

# słownik - para klucz:wartosc
# {'name': 'John', 'age': 30, "car": None}
# odpowiednik jsona

pusty_slownik = {}
print(type(pusty_slownik))  # <class 'dict'>
print(pusty_slownik)  # {}

pusty_slownik = dict()
print(type(pusty_slownik))
print(pusty_slownik)
# <class 'dict'>
# {}

osoba = {
    "id": 89,
    'imie': "Tadeusz",
    "rok": 1976,
    "miasto": "Łódź"
}

print(osoba)
# {'id': 89, 'imie': 'Tadeusz', 'rok': 1976, 'miasto': 'Łódź'}
print(type(osoba))  # <class 'dict'>

print(osoba['miasto'])  # Łódź
# print(osoba['Miasto'])  # KeyError: 'Miasto'

print(osoba.get("miasto"))
print(osoba.get("Miasto"))  # None
print(osoba.get("Miasto", "default"))  # default

osoba['imie'] = "Radek"  # nadpisze
print(osoba)
# {'id': 89, 'imie': 'Radek', 'rok': 1976, 'miasto': 'Łódź'}

print(osoba.keys())
print(osoba.values())
print(osoba.items())

# dict_keys(['id', 'imie', 'rok', 'miasto'])
# dict_values([89, 'Radek', 1976, 'Łódź'])
# dict_items([('id', 89), ('imie', 'Radek'), ('rok', 1976), ('miasto', 'Łódź')])

lista = [1, 2, 3, 4, 4, 7, 7, 6, 5, 1, 3, 4, 5, 6, 7, "A"]

print(dict.fromkeys(lista))
# {1: None, 2: None, 3: None, 4: None, 7: None, 6: None, 5: None, 'A': None}
print(list(dict.fromkeys(lista)))  # [1, 2, 3, 4, 7, 6, 5, 'A']

# pętla for
for i in range(5):
    print(i)

#
for i in nowa_lista:
    print(i)
    # Jan
    # Piotr
    # Anna
    # Michał
    # Radek

# 0 Radek -> 111 Radek

imen = enumerate(nowa_lista, start=111)
print(imen)  # <enumerate object at 0x000001B149EBD030>
# for i in imen:
#     print(i)
# # (111, 'Jan')
# # (112, 'Piotr')
# # (113, 'Anna')
# # (114, 'Michał')
# # (115, 'Radek')
#
# dane = (115, 'Radek')
# a = dane[0]
# b = dane[1]
#
# a, b = (115, 'Radek')
# print(a, b) # (115, 'Radek')
# # 115 Radek

print(40 * "-")
for index, wartosc in imen:
    print(f"index -> {index}, wartosc => {wartosc}")
# ----------------------------------------
# index -> 111, wartosc => Jan
# index -> 112, wartosc => Piotr
# index -> 113, wartosc => Anna
# index -> 114, wartosc => Michał
# index -> 115, wartosc => Radek

print("index -> {}, wartosc => {}".format(index, wartosc))  # index -> 115, wartosc => Radek
print("index ->", index, "wartosc =>", wartosc)  # index -> 115 wartosc => Radek
