# __iter__, __next__

class Count:
    def __init__(self, lows, high):
        """
        itertor liczacy w zadanym zakresie
        :param lows:
        :param high:
        """
        self.current = lows
        self.highs = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.highs:
            raise StopIteration
        else:
            self.current += 1
            return self.current


print(25 * "-")
counter = Count(1, 5)
print(next(counter))
print(next(counter))
print(next(counter))
# -------------------------
# 2
# 3
# 4
print(next(counter))
print(next(counter))
try:
    print(next(counter))
except StopIteration:
    print("Koniec")  # Koniec
