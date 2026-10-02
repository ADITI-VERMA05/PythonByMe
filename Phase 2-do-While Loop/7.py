'''7. Check whether the given number is a palindrome.'''


num = int(input("Enter a number: "))
temp = abs(num)
rev = 0

while True:
    digit = temp % 10
    rev = (rev * 10) + digit
    temp //= 10
    if temp == 0:
        break

if num >= 0 and num == rev:
    print(f"{num} is a Palindrome.")
else:
    print(f"{num} is NOT a Palindrome.")