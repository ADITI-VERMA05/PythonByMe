'''19. Find and print the sum of the first n natural numbers.'''

n = int(input("Enter a number: "))
sum_of_natural_numbers = 0
for i in range(1, n + 1):
    sum_of_natural_numbers += i