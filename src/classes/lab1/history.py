
history = []

def add_to_history(x, y, action, result):
    history.append(f'{x} {action} {y} = {result}')

def show_history():
    if history:
        print("\nHISTORY:")
        for entry in history:
            print(f"\t {entry}")
        print("\n")
    else:
        print('# no history available.')
