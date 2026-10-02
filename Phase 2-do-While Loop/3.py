'''3. Keep taking numbers from the user until 0 is entered, then print the sum of all entered numbers.'''

total_sum = 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total_sum += num

print(f"Total Sum: {total_sum}")