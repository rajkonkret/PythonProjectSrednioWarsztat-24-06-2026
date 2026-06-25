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


print(20 * "-")


def gen4():
    i = 1
    while True:
        yield i * i
        i += 1


generator4 = gen4()
print(next(generator4))
print(next(generator4))
print(next(generator4))
print(next(generator4))
print(next(generator4))

generator4.close()


def gen5():
    i = 1
    while True:
        command = yield i * i
        print(command)  # None, OK
        if command == "OK":
            print("Jestem generatorem...")
        elif command == "stop":
            break
        i += 1


generator5 = gen5()
print(next(generator5))
print(next(generator5))
print(next(generator5))
print(next(generator5))
generator5.send("OK")
print(next(generator5))  # None


# generator5.send("stop")  # StopIteration

def fibo_with_index(n):
    a, b = 0, 1  # a=0, b=1
    for ind in range(n):
        yield ind, a
        a, b = b, a + b  # a = b, b = a + b


fib = fibo_with_index(10)
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
# (0, 0)
# (1, 1)
# (2, 1)
# (3, 2)
a, b = 1, 2
b, a = a, b
print(b, a)  # 1 2
print(25 * "-")
for i, n in fibo_with_index(5):
    print(f"Pozycja: {i}, element: {n}")
# -------------------------
# Pozycja: 0, element: 0
# Pozycja: 1, element: 1
# Pozycja: 2, element: 1
# Pozycja: 3, element: 2
# Pozycja: 4, element: 3
