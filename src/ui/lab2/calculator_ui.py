"""
This module contains the CalculatorUI class, which handles the user interface
for the calculator, including displaying the layout, asking for input, and
showing results.
"""

from src.const.const import USER_PROMPT_WITH_VALUES, CALCULATE_COMPLETE_MESSAGE, CONTINUE_CHOICE_PROMPT, \
    OPERATION_CHOICE_PROMPT


class CalculatorUI:
    """
    A class to represent the user interface for the calculator application.

    Methods:
        display_layout: Displays the layout of the calculator interface.
        ask_number: Prompts the user to enter a number.
        ask_operator: Prompts the user to select an operator.
        show_result: Displays the result of the calculation.
        show_error: Displays an error message.
        ask_again: Prompts the user to continue or exit the calculator.
    """

    def display_layout(self):
        """
        Displays the layout of the calculator interface.
        """
        layout = (
            "\n"
            "+   -   *   \n"
            "7   8   9   ^\n"
            "4   5   6   √\n"
            "1   2   3   %\n"
            "0   .\n"
        )
        return layout

    def ask_number(self, variable_name):
        """
        Prompts the user to enter a number.

        Args:
            variable_name (str): The name of the variable (e.g., 'x', 'y').

        Returns:
            str: The user input number as a string.
        """
        return input(f"{USER_PROMPT_WITH_VALUES} {variable_name}: ")

    def ask_operator(self):
        """
        Prompts the user to select an operator.

        Returns:
            str: The selected operator.
        """
        return input(OPERATION_CHOICE_PROMPT)

    def show_result(self, result):
        """
        Displays the result of the calculation.

        Args:
            result (float or str): The result of the calculation to be displayed.
        """
        print(f"{CALCULATE_COMPLETE_MESSAGE}{result}")

    def show_error(self, message):
        """
        Displays an error message.

        Args:
            message (str): The error message to be displayed.
        """
        print(message)

    def ask_again(self):
        """
        Prompts the user to continue or exit the calculator.

        Returns:
            bool: True if the user wants to continue, False otherwise.
        """
        return input(CONTINUE_CHOICE_PROMPT).lower() == "y"
