'''6. Reverse the given number and print the reversed value.'''

num = int(input("Enter a number: "))
temp = abs(num)
rev = 0

while True:
    digit = temp % 10
    rev = (rev * 10) + digit
    temp //= 10
    if temp == 0:
        break

if num < 0:
    rev = -rev

print(f"Reversed Number: {rev}")