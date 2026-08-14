'''20. Find and print the sum of the Fibonacci series up to n terms.'''

n = int(input("Enter the number of terms: "))
a, b = 0, 1
sum_fib = 0
i = 0
while i < n:
    sum_fib += a
    a, b = b, a + b
    i += 1
print("The sum of the Fibonacci series up to", n, "terms is:", sum_fib)
