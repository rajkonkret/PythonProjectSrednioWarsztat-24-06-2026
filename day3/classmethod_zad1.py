# classmethod


class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    @classmethod
    def z_nazwy_pelnej(cls, nazwa_pelna):
        imie, nazwisko = nazwa_pelna.split()
        return cls(imie, nazwisko)


osoba1 = Osoba("Jan", "Kowalski")
print(osoba1.imie, osoba1.nazwisko)  # Jan Kowalski
dane = "Jan Kowalski"
name, surname = dane.split()
osoba2 = Osoba(name, surname)
print(osoba2.imie)  # Jan

osoba3 = Osoba.z_nazwy_pelnej(dane)
print(osoba3.imie)
print(osoba3.nazwisko)
# Jan
# Kowalski
