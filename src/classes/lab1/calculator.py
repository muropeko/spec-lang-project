
def format_result(result, decimal_places):
    return f'{result:.{decimal_places}f}' if isinstance(result, (int, float)) else result

def memory_clear():
    return 0, '~ memory cleared'

def memory_store(value, decimal_places):
    return value, f'~ memory saved: {format_result(value, decimal_places)}'

def memory_add(memory, value, decimal_places):
    updated_memory = memory + value
    return updated_memory, f'~ memory updated: {format_result(updated_memory, decimal_places)}'

def calc(x, y, action, memory, extended, decimal_places):
    actions = {
        'MC': memory_clear,
        'MR': lambda: (memory, format_result(memory, decimal_places)),
        'MS': lambda: memory_store(x, decimal_places),
        'M+': lambda: memory_add(memory, x, decimal_places),
        '+': lambda: (memory, format_result(x + y, decimal_places)),
        '-': lambda: (memory, format_result(x - y, decimal_places)),
        '*': lambda: (memory, format_result(x * y, decimal_places)),
        '/': lambda: (memory, 'error: divide by zero' if y == 0 else format_result(x / y, decimal_places)),
        '%': lambda: (memory, 'error: divide by zero' if y == 0 else format_result(x % y, decimal_places)),
        '^': lambda: (memory, format_result(x ** y, decimal_places)),
        '√': lambda: (memory, 'error: root of zero' if y == 0 else format_result(x ** (1 / y), decimal_places)),
    }

    if not extended and action in {'^', '√', '%', 'MC', 'MR', 'MS', 'M+'}:
        return memory, '! error: operation is not allowed in non-extended mode'

    return actions.get(action, lambda: (memory, 'unknown action'))()
