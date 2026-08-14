'''14. Find and print the sum of digits of the given number.'''

num = int(input("Enter a number: "))
sum_of_digits = 0
while num > 0:
    digit = num % 10 # Extracts the last digit of the number using the modulus operator.
    sum_of_digits += digit # Adds the extracted digit to the sum_of_digits variable.
    num //= 10 # Removes the last digit from the original number using floor division.
print(f"The sum of digits of the given number is: {sum_of_digits}")
