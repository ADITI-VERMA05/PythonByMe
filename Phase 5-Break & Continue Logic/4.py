'''4. Search for a specific number in a list of inputs, and terminate the loop immediately when the number is found.'''

target_number = float(input("Enter the number to search for: "))
found = False

print("Please enter 5 numbers:")

for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    
    if num == target_number:
        print(f"Number {target_number} found!")
        found = True
        break

if not found:
    print(f"Number {target_number} not found.")