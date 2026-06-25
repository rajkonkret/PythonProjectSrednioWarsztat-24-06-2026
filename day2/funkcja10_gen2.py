import time


def wznowienie(n, k):
    print("Wstrzymanie diałania...")
    yield 1001

    print("Kolejny krok")
    yield n + k

    print("Krok ostatni")
    yield n * k

print(20 * "-")
