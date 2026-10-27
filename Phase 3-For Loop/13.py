'''13. Find and print the sum of all factors of the given number.'''

num = int(input("Enter a number: "))
print("Sum of factors of", num, "is:")
sum_of_factors = 0
for i in range(1, num + 1):
    if num % i == 0:
        sum_of_factors += i
print(sum_of_factors)