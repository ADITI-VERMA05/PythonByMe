'''14. Find and print the sum of digits of the given number.'''

num = abs(int(input("Enter a number: ")))
temp = num
digit_sum = 0

while True:
    digit = temp % 10
    digit_sum += digit
    temp //= 10
    if temp == 0:
        break

print(f"Sum of digits: {digit_sum}")