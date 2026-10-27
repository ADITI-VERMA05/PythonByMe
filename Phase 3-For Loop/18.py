'''18. Print all numbers between a and b that are divisible by 7.'''

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("Numbers between", a, "and", b, "that are divisible by 7 are:")
for i in range(a, b + 1):
    if i % 7 == 0:
        print(i)
        