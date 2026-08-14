'''6. Calculate and print the sum of the first n natural numbers.'''

n = int(input("Enter a number: "))
sum = 0
for i  in range(1, n + 1):
    sum += i
print(f"The sum of the first {n} natural numbers is: {sum}")
