'''29. Find the largest digit in the given number.'''


num = int(input("Enter a number: "))
largest_digit = 0  # Initialize with the largest single digit

while num != 0:
    digit = num % 10
    if digit > largest_digit:
        largest_digit = digit
    num = num // 10

print("The largest digit in the given number is:", largest_digit)