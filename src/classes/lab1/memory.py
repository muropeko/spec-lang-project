def memory_clear():
    return 0, '~ memory cleared'

def memory_store(value, format_result):
    return value, f'~ memory saved: {format_result(value)}'

def memory_add(memory, value, format_result):
    updated_memory = memory + value
    return updated_memory, f'~ memory updated: {format_result(updated_memory)}'
