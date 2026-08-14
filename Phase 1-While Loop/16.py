'''16. Check whether the given number is a Perfect number.'''
# A Perfect number is a positive integer that is equal to the sum of its positive divisors, 
# excluding the number itself.

n = int(input("Enter a number: "))
sum_of_divisors = 0
i = 1
while i < n:
    if n % i == 0:
        sum_of_divisors += i
    i += 1
    
if sum_of_divisors == n:
    print(f"{n} is a Perfect number.")
else:
    print(f"{n} is not a Perfect number.")
    