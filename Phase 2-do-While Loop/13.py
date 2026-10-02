'''13. Keep taking numbers from the user until a negative number is entered, then count how many positive numbers were entered.'''

count = 0
while True:
    num = int(input("Enter a number: "))
    if num < 0:
        break
    if num > 0:
        count += 1

print(f"Total Positive Numbers Entered: {count}")