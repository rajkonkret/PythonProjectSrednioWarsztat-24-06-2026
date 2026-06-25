from functools import reduce

transactions = [
    {'id': 1, "type": "income", "amount": 1000, "currency": "USD"},
    {'id': 2, "type": "expense", "amount": 200, "currency": "USD"},
    {'id': 3, "type": "income", "amount": 500, "currency": "USD"},
    {'id': 4, "type": "expense", "amount": 300, "currency": "USD"},
    {'id': 5, "type": "income", "amount": 700, "currency": "USD"},
    {'id': 6, "type": "expense", "amount": 400, "currency": "EUR"},
    {'id': 7, "type": "income", "amount": 100, "currency": "EUR"},
]


# filter()
# map()
# reduce()

def filter_transactions(transactions, transction_type):
    """
    filtruje transakcje po typie transakcji: income, expense
    :param transactions:
    :param transction_type:
    :return: lista transakcji
    """
    return list(filter(lambda x: x['type'] == transction_type, transactions))


def map_transactions(transactions, currency):
    """
    Mapuje transakcje spełniające warunek waluty
    :param transactions:
    :param currency:
    :return:
    """
    return list(map(lambda x: x['amount'] if x['currency'] == currency else 0, transactions))


# [400,0,0]

def reduce_transactions(mapped):
    """
    Zsumuje kwoty transakcji
    :param mapped:
    :return:
    """
    return reduce(lambda x, y: x + y, mapped, 0)


def process_transactions(transactions, transaction_type, currency):
    """
    przetwarza tramnsakcje
    :param transactions:
    :param transaction_type:
    :param currency:
    :return:
    """
    filtered = filter_transactions(transactions, transaction_type)
    mapped = map_transactions(filtered, currency)
    total = reduce_transactions(mapped)

    return total
    # print(total)


def test_transactions_processing():
    assert (map_transactions(filter_transactions(transactions, "income"), "USD")
            == [1000, 500, 700, 0])


# pip install pytest
if __name__ == '__main__':

    print(process_transactions(transactions, "expense", "EUR"))  # 400



# (.venv) PS C:\Users\CSComarch\PycharmProjects\PythonProject\day2> pytest -v .\transakcje.py
# ======================================================================= test session starts ========================================================================
# platform win32 -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\CSComarch\PycharmProjects\PythonProject\.venv\Scripts\python.exe
# cachedir: .pytest_cache
# rootdir: C:\Users\CSComarch\PycharmProjects\PythonProject\day2
# collected 1 item
#
# transakcje.py::test_transactions_processing PASSED                                                                                                            [100%]
#
# ======================================================================== 1 passed in 0.01s =========================================================================
# (.venv) PS C:\Users\CSComarch\PycharmProjects\PythonProject\day2>
