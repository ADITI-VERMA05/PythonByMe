'''8. Check whether the given number is an Armstrong number.'''

num = int(input("Enter a number: "))
temp = abs(num)

# Count digits first
num_digits = len(str(temp))
armstrong_sum = 0

while True:
    digit = temp % 10
    armstrong_sum += digit ** num_digits
    temp //= 10
    if temp == 0:
        break

if num == armstrong_sum:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is NOT an Armstrong number.")