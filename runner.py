from src.classes.lab1 import main as lab1
from src.classes.lab2 import main as lab2
from src.classes.lab3 import main as lab3
from src.classes.lab4 import main as lab4
from src.classes.lab5 import main as lab5
from src.classes.lab7 import main as lab7
from src.classes.lab8 import main as lab8

def display_menu():
    print("\nChoose lab:\n"
        "\t1. Lab1\n"
        "\t2. Lab2\n"
        "\t3. Lab3\n"
        "\t4. Lab4\n"
        "\t5. Lab5\n"
        "\t7. Lab7\n"
        "\t8. Lab8\n"
        "\t0. exit\n")

def main():
    options = {
        '1': lab1.main,
        '2': lab2.main,
        '3': lab3.main,
        '4': lab4.main,
        '5': lab5.main,
        '7': lab7.main,
        '8': lab8.main,
        '0': lambda: print("Exiting program...")
    }

    while True:
        print("-----------")
        display_menu()
        user_input = input('Enter number: ')

        action = options.get(user_input, lambda: print("Invalid option. Please choose again."))
        action()

        if user_input == '0':
            break


if __name__ == "__main__":
    main()
