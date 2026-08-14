'''28. Find the smallest digit in the given number.'''

num = int(input("Enter a number: "))
smallest_digit = 9  # Initialize with the largest single digit

while num != 0:
    digit = num % 10
    if digit < smallest_digit:
        smallest_digit = digit
    num = num // 10

print("The smallest digit in the given number is:", smallest_digit)