import unittest


def divide(a, b):
    return a / b


# PascalCase
class TestDivide(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(10, 2), 6)


# C:\Program Files\JetBrains\PyCharm 2026.1.3\plugins\python-ce\helpers\pycharm\teamcity\diff_tools.py:33: in _patched_equals
#     old(self, first, second, msg)
# E   AssertionError: 5.0 != 6
# Expected :5.0
# Actual   :6

if __name__ == '__main__':
    unittest.main()
