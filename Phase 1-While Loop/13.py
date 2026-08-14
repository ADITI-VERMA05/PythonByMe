'''13. Check whether the given number is a palindrome.'''

num = int(input("Enter a number: "))
reversed_num = 0
n = num
while n > 0:
    digit = n % 10 # Extracts the last digit of the number using the modulus operator.
    reversed_num = reversed_num * 10 + digit # Appends the extracted digit to the reversed number 
                        # by multiplying the current reversed number by 10 and adding the new digit.
    n //= 10 # Removes the last digit from the original number using floor division.
if reversed_num == num:
    print(f"The given number ie. {num} is a palindrome.")
else:
    print(f"The given number ie. {num} is not a palindrome.")