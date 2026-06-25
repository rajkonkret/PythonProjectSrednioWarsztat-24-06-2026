import time


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
