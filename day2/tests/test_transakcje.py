# assert - asercja - test
x = 5
assert x == 5

# assert x == 15
# (.venv) PS C:\Users\CSComarch\PycharmProjects\PythonProject\day2> python .\tests\test_transakcje.py
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\PythonProject\day2\tests\test_transakcje.py", line 5, in <module>
#     assert x == 15
#            ^^^^^^^
# AssertionError

import transakcje as tr


def test_map_transactions_usd():
    result = [1000, 200, 500, 300, 700, 0, 0]
    assert tr.map_transactions(tr.transactions, "USD") == result


# tests/test_transakcje.py::test_map_transactions_usd PASSED

def test_reduce_transactions():
    assert tr.reduce_transactions([1000, 500, 700, 0]) == 2200
# day2/tests/test_transakcje.py::test_map_transactions_usd PASSED          [ 50%]
# day2/tests/test_transakcje.py::test_reduce_transactions PASSED           [100%]