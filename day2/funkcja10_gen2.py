import time


def wznowienie(n, k):
    print("Wstrzymanie diałania...")
    yield 1001

    print("Kolejny krok")
    yield n + k

    print("Krok ostatni")
    yield n * k


print(20 * "-")
for i in wznowienie(6, 8):
    if i == 1001:
        continue
    time.sleep(1)
    print(f"Yield zwraca wartości: {i}")
# --------------------
# Wstrzymanie diałania...
# Kolejny krok
# Yield zwraca wartości: 14
# Krok ostatni
# Yield zwraca wartości: 48
