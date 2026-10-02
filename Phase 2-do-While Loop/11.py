''' 11. Find the HCF (Highest Common Factor) of the given numbers.'''

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x, y = abs(a), abs(b)

while True:
    if y == 0:
        break
    x, y = y, x % y

print(f"HCF of {a} and {b} is {x}")