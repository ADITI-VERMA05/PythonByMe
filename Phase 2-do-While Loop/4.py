''' 4. Keep taking numbers from the user until 0 is entered, then print the largest number among all inputs.'''

max_num = None
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    if max_num is None or num > max_num:
        max_num = num

if max_num is not None:
    print(f"Largest Number: {max_num}")
else:
    print("No numbers were entered.")