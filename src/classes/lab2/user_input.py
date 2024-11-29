from src.const.const import INVALID_VALUE_MESSAGE, INVALID_CHOICE_MESSAGE


class UserInput:

    def __init__(self, ui):
        self.ui = ui

    def get_number(self, variable_name):
        while True:
            try:
                return float(self.ui.ask_number(variable_name))
            except ValueError:
                self.ui.show_error(f"\t{INVALID_VALUE_MESSAGE}")

    def get_operator(self):
        valid_operators = {"+", "-", "*", "/", "^", "%", "√"}
        while True:
            operator = self.ui.ask_operator()
            if operator not in valid_operators:
                self.ui.show_error(f"\t{INVALID_CHOICE_MESSAGE}")
            else:
                return operator
