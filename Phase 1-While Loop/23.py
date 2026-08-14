'''23. Print all numbers between a and b that are divisible by 7.'''

a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))
i = a
while i <= b:
    if i % 7 == 0:
        print(i, end=" ")
    i += 1
    