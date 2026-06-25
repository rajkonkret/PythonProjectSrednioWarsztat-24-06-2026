# funkcja rekurencyjna
# funkcja wywołuja sama siebie
from functools import lru_cache


def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n - 1)


print(silnia(5))  # 120


@lru_cache(maxsize=512)
def fibonacci(n):
    if n < 0:
        raise ValueError("n nie może byc ujemne")

    if n < 2:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci.cache_info())
# CacheInfo(hits=0, misses=0, maxsize=512, currsize=0)
print(fibonacci(5))  # 55
print(fibonacci.cache_info())

print(fibonacci.cache_info())
# CacheInfo(hits=3, misses=6, maxsize=512, currsize=6)
print(fibonacci(10))  # 55
print(fibonacci.cache_info())
# CacheInfo(hits=9, misses=11, maxsize=512, currsize=11)

# zsumowac wszystkie wartosci ze słownika
nested_data = {
    "a": 1,
    "b": {
        "c": 2,
        "d": [3, 4, {"e": 5}]
    },
    "f": [6, 7]
}


def sum_nested(data):
    total = 0

    if isinstance(data, dict):
        for value in data.values():
            total += sum_nested(value)
    elif isinstance(data, list):
        for item in data:
            total += sum_nested(item)
    elif isinstance(data, (int, float)):
        total += data

    return total

result = sum_nested(nested_data)
print(result) # 28