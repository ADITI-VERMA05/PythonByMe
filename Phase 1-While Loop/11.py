'''11. Count and print the total number of digits in a given number.'''

n = int(input("Enter a number: "))
count = 0
while n > 0:
    n //= 10 # Removes the last digit from the original number using floor division.
    count += 1 # Increments the count variable by 1 for each digit removed from the number.
print(f"The total number of digits in the given number ie. {n} is: {count}")