'''15. Calculate and print the sum of even digits and the sum of odd digits of the given number separately'''

num = abs(int(input("Enter a number: ")))
temp = num
even_sum = 0
odd_sum = 0

while True:
    digit = temp % 10
    if digit % 2 == 0:
        even_sum += digit
    else:
        odd_sum += digit
    temp //= 10
    if temp == 0:
        break

print(f"Sum of Even Digits: {even_sum}")
print(f"Sum of Odd Digits: {odd_sum}")