from .operations import Operations
from src.classes.lab2.operations import Operations
from src.ui.lab2.calculator_ui import CalculatorUI
from src.classes.lab2.user_input import UserInput
from src.const.const import DIVISION_BY_ZERO_MESSAGE

class Calculator:

    def __init__(self):
        self.ui = CalculatorUI()
        self.user_input = UserInput(self.ui)
        self.operations = Operations()

    def run(self):
        while True:
            print(self.ui.display_layout())

            x = self.user_input.get_number("x")
            operator = self.user_input.get_operator()
            y = self.user_input.get_number("y") if operator != "√" else None

            result = self.operations.calculate(x, y, operator)
            self.ui.show_result(result)

            if not self.ui.ask_again():
                break
