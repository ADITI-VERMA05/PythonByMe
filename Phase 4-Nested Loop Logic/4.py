'''4. Print all prime numbers up to n using nested loop checking.'''

n = int(input("Enter a number: "))
print(f"Prime numbers up to {n} are:")
for i in range(2, n + 1):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i, end=" ")