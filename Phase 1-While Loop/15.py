'''15. Check whether the given number is an Armstrong number.'''
# An Armstrong number (also known as a narcissistic number) is a number that equals the sum of its own digits
#  each raised to the power of the number of digits. Example: 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.

n = int(input("Enter a number: "))
# Store the original number to compare later
original_num = n
# Calculate the number of digits in the number
num_digits = 0
temp = n
while temp > 0:
    temp //= 10 # Removes the last digit from the original number using floor division.
    num_digits += 1 # Increments the num_digits variable by 1 for each digit removed from the number.
    
# Calculate the sum of the digits raised to the power of num_digits
sum_of_powers = 0
while n > 0:
    digit = n % 10 # Extracts the last digit of the number using the modulus operator.
    sum_of_powers += digit ** num_digits # Raises the extracted digit to the power of num_digits and 
                                        # adds it to the sum_of_powers variable.
    n //= 10 # Removes the last digit from the original number using floor division.
    
# Check if the number is an Armstrong number
if sum_of_powers == original_num:
    print(f"{original_num} is an Armstrong number.")
else:
    print(f"{original_num} is not an Armstrong number.")
    