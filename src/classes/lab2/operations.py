import math
from src.const.const import DIVISION_BY_ZERO_MESSAGE, NEGATIVE_NUMBER_MESSAGE


class Operations:
    def __init__(self):
        self._operations = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": self._safe_division,
            "^": lambda x, y: x ** y,
            "%": lambda x, y: x % y,
            "√": self._safe_sqrt
        }

    def _safe_division(self, x, y):
        if y == 0:
            return DIVISION_BY_ZERO_MESSAGE
        return x / y

    def _safe_sqrt(self, x):
        if x < 0:
            return NEGATIVE_NUMBER_MESSAGE
        return math.sqrt(x)

    def calculate(self, x, y, operator):
        if operator == "√":
            return self._operations[operator](x)
        return self._operations[operator](x, y)
