'''20. Find and print the sum of all even numbers from 1 up to n.'''

n = int(input("Enter a number: "))
sum_of_even_numbers = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        sum_of_even_numbers += i
print("Sum of all even numbers from 1 up to", n, "is:", sum_of_even_numbers)