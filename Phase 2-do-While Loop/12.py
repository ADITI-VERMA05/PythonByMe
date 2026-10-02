''' 12. Create a menu-driven program that allows the user to choose and perform different operations.'''

while True:
    print("\n--- MENU ---")
    print("1. Add Two Numbers")
    print("2. Subtract Two Numbers")
    print("3. Multiply Two Numbers")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        print(f"Result: {x + y}")
    elif choice == '2':
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        print(f"Result: {x - y}")
    elif choice == '3':
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        print(f"Result: {x * y}")
    elif choice == '4':
        print("Exiting Program...")
        break
    else:
        print("Invalid Choice! Try again.")