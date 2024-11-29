
def change_settings(decimal_places, memory):
    while True:
        print("\n\tSETTINGS")
        print("1. change decimal")
        print("2. reset memory")
        print("3. return")
        choice = input("\tSelect an option: ").strip()

        if choice == '1':
            try:
                decimal_places = int(input("\n# enter the number of decimal: ").strip())
                if decimal_places < 0:
                    print("! decimal must be greater than 0")
                    decimal_places = 2
                print(f"~ decimal set to {decimal_places}\n")
            except ValueError:
                print("! invalid input")

        elif choice == '2':
            memory = 0
            print("~ memory has been reset.")
        elif choice == '3':
            break
        else:
            print("! invalid input")

    return decimal_places, memory
