# ui.py

def display_layout(extended):
    layout = (
        "MC  C   X   %   /   ^n\n"
        "MR  7   8   9   *   √\n"
        "MS  4   5   6   -   %\n"
        "M+  1   2   3   +\n"
        "ext 0   ."
    ) if extended else (
        "C   X   %   /\n"
        "7   8   9   *\n"
        "4   5   6   -\n"
        "1   2   3   +\n"
        "ext 0   ."
    )
    print("\n" + layout)

def get_number(prompt):
    while True:
        try:
            value = input(prompt)
            if value.lower() == 'ext':
                return 'ext'
            return float(value)
        except ValueError:
            print('! not a number')



from src.classes.lab1.calculator import calc, format_result
from src.classes.lab1.history import add_to_history, show_history
from src.classes.lab1.settings import change_settings

def main():
    memory = 0
    extended = False
    decimal_places = 2

    while True:
        display_layout(extended)
        action = input('\n# enter "settings" to configure or "calculate" to perform a calculation: ').strip().lower()

        if action == 'settings':
            decimal_places, memory = change_settings(decimal_places, memory)
            continue

        elif action == 'calculate':
            x = get_number('x: ')
            if x == 'ext':
                extended = not extended
                display_layout(extended)
                continue
            y = get_number('y: ')
            if y == 'ext':
                extended = not extended
                display_layout(extended)
                continue

            operation_prompt = '# operation (+, -, /, *, %, ^, √): ' if extended else '# operation (+, -, /, *): '
            operation = input(operation_prompt)

            memory, result = calc(x, y, operation, memory, extended, decimal_places)
            result = format_result(result, decimal_places)
            add_to_history(x, y, operation, result)
            print(f'# result: {result}')

            choice = input('\n# continue? (y/n), or type "history" to view history: ').strip().lower()
            if choice == 'n':
                print('# exiting...')
                break
            elif choice == 'history':
                show_history()

        else:
            print("! invalid option")

if __name__ == '__main__':
    main()
