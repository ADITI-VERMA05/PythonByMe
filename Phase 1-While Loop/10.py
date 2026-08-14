'''10. Find and print the product of all digits of a given number.'''

n = int(input("Enter a number: "))
product = 1
while n > 0:
    digit = n % 10  # Isolates the last digit of the number using the remainder (modulo) operator.
    product *= digit # Multiplies the isolated digit into a running total variable called product.
    n //= 10 # Removes the last digit from the original number using floor division.
print(f"The product of all digits of {n} is: {product}")