'''10. Print the Fibonacci series up to the required number of terms.'''

n = int(input("Enter number of terms: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    a, b = 0, 1
    count = 0
    while True:
        print(a, end=" ")
        a, b = b, a + b
        count += 1
        if count >= n:
            break
    print()