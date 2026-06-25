# assert - asercja - test
import pytest

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


def test_filter_transactions_income():
    expected_list = [
        {'id': 1, "type": "income", "amount": 1000, "currency": "USD"},

        {'id': 3, "type": "income", "amount": 500, "currency": "USD"},

        {'id': 5, "type": "income", "amount": 700, "currency": "USD"},

        {'id': 7, "type": "income", "amount": 100, "currency": "EUR"},
    ]

    assert tr.filter_transactions(tr.transactions, "income") == expected_list


# tests/test_transakcje.py::test_map_transactions_usd PASSED                                                                                                    [ 33%]
# tests/test_transakcje.py::test_reduce_transactions PASSED                                                                                                     [ 66%]
# tests/test_transakcje.py::test_filter_transactions_income PASSED                                                                                              [100%]


# testy parametryzowany
@pytest.mark.parametrize(
    "kind,currency,expected",
    [
        ("income", "USD", 1000 + 500 + 700),
        ("income", "EUR", 100),
        ("expense", "USD", 200 + 300),
        ("expense", "EUR", 400),
    ]
)
def test_process_transactions_param(kind, currency, expected):
    assert tr.process_transactions(tr.transactions, kind, currency) == expected

# collected 7 items
#
# tests/test_transakcje.py::test_map_transactions_usd PASSED                                                                                                    [ 14%]
# tests/test_transakcje.py::test_reduce_transactions PASSED                                                                                                     [ 28%]
# tests/test_transakcje.py::test_filter_transactions_income PASSED                                                                                              [ 42%]
# tests/test_transakcje.py::test_process_transactions_param[income-USD-2200] PASSED                                                                             [ 57%]
# tests/test_transakcje.py::test_process_transactions_param[income-EUR-100] PASSED                                                                              [ 71%]
# tests/test_transakcje.py::test_process_transactions_param[expense-USD-500] PASSED                                                                             [ 85%]
# tests/test_transakcje.py::test_process_transactions_param[expense-EUR-400] PASSED                                                                             [100%]