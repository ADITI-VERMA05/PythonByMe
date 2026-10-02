''' 5. Count and print the number of digits in the given number.'''

num = abs(int(input("Enter a number: ")))
temp = num
count = 0

while True:
    count += 1
    temp //= 10
    if temp == 0:
        break

print(f"Total Digits: {count}")