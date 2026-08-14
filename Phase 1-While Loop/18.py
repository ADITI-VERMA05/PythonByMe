'''18. Check whether the given number is a prime number.'''

n = int(input("Enter a number: "))
if n > 1:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print(n, "is not a prime number.")
            break
    else:
        print(n, "is a prime number.")