import time
import numpy as np


# pip install numpy
# numpy - biblioteka do działań na tablicach/macierzach ndarray

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        ex_time = time.perf_counter() - start_time

        print(f"Czas wykonania funkcji: {func.__name__}: {ex_time}")

        return result

    return wrapper


lista1 = list(range(10_000_000))
lista2 = list(range(10_000_000))

array1 = np.arange(10_000_000, dtype=np.int64)
array2 = np.arange(10_000_000, dtype=np.int64)


@measure_time
def my_time():
    time.sleep(2)


@measure_time
def add_with_for():
    result = []
    for i in range(len(lista1)):
        suma = lista1[i] + lista2[i]
        result.append(suma)
    return "OK For"


@measure_time
def add_lc():
    result = [lista1[i] + lista2[i] for i in lista1]
    return "OK LC"


# zip() - łączy kolekcje
@measure_time
def add_zip():
    result = [a + b for a, b in zip(lista1, lista2)]
    return "OK ZIP"
    # (1, 3) -> a, b -> a + b


@measure_time
def add_np():
    result = array1 + array2  # broadcasting
    return "OK np"


my_time()  # Czas wykonania funkcji: my_time: 2.0002292999997735
add_with_for()  # Czas wykonania funkcji: add_with_for: 1.8390606000029948
add_lc()  # Czas wykonania funkcji: add_lc: 1.3834720999875572
add_zip()  # Czas wykonania funkcji: add_zip: 1.2276006000174675
add_np()  # Czas wykonania funkcji: add_np: 0.0433445000089705
