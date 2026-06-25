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
