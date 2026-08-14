'''12. Reverse the given number and print the reversed value.'''

n = int(input("Enter a number: "))
reversed_num = 0
while n > 0:
    digit = n % 10 # Extracts the last digit of the number using the modulus operator.
    reversed_num = reversed_num * 10 + digit # Appends the extracted digit to the reversed number 
                        # by multiplying the current reversed number by 10 and adding the new digit.
    n //= 10 # Removes the last digit from the original number using floor division.
print(f"The reversed number is: {reversed_num}")