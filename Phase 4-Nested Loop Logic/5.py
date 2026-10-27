'''5. Print the Fibonacci pattern row by row, where each row prints the next Fibonacci numbers.'''

n = int(input("Enter the number of rows for the Fibonacci pattern: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b