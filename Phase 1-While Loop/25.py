'''25. Find and print the sum of all factors of the given number'''

n = int(input("Enter a number: "))
sum_of_factors = 0
for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        sum_of_factors += i
        if i != n // i:
            sum_of_factors += n // i

print("Sum of factors of", n, "is:", sum_of_factors)