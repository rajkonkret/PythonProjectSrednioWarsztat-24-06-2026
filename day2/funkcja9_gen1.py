# generator - generuje dane kiedy są potrzebne
# lazy
import time


def kwadrat(n):
    for x in range(n):
        print(x ** 2)


kwadrat(5)


def kwadrat_gen(n):
    for x in range(n):  # 0,1,2,3,4
        yield x ** 2  # zwraca wynik, zatrzymuje działąnie, pamięta gdzie skonczył


kwa = kwadrat_gen(10)
print(kwa)  # <generator object kwadrat_gen at 0x0000021565F50EE0>

# next() - wypisz kolejny element danych
print(next(kwa))
print(next(kwa))
print(next(kwa))
print(next(kwa))

print(("Zrób cokolwiek"))
print(("Zrób cokolwiek"))
print(("Zrób cokolwiek"))

print(next(kwa))
# 9
# Zrób cokolwiek
# Zrób cokolwiek
# Zrób cokolwiek
# 16
print(next(kwa))
print(next(kwa))
print(next(kwa))
print(next(kwa))
print(next(kwa))
# print(next(kwa)) # StopIteration - koniec danych
try:
    print(next(kwa))
except StopIteration:
    print("Koniec danych")

kwa2 = kwadrat_gen(10)

for k in kwa2:
    print(k)
    print("Pretwarzanie danch...")
    time.sleep(1)
# 81
# Pretwarzanie danch...

kwa3 = kwadrat_gen(5)
kwa4 = kwadrat_gen(5)

print(next(kwa3))
print(next(kwa3))
print(next(kwa3))

print(next(kwa4))
print(next(kwa4))
print(next(kwa4))

print(next(kwa3))
