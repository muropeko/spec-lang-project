class UserInput:
    @staticmethod
    def get_input(prompt, choices=None):
        while True:
            value = input(prompt).strip().lower()
            if not value:
                print(f"\t! invalid value")
                continue
            if choices and value not in choices:
                formatted_choices = ", ".join(choices)
                print(f"\t! incorrect choice. options: {formatted_choices}")
            else:
                return value

    @staticmethod
    def get_integer_input(prompt, min_value, max_value):
        while True:
            value = input(prompt).strip()
            if not value:
                print(f"\t! invalid value")
                continue
            try:
                value = int(value)
                if min_value <= value <= max_value:
                    return value
                else:
                    print(f"\t! value is out of a range ({min_value} - {max_value})")
            except ValueError:
                print(f"\t! invalid value")
