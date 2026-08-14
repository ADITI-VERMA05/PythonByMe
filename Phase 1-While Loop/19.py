'''19. Print the Fibonacci series up to n terms.'''

n = int(input("Enter the number of terms: "))
a, b = 0, 1
i = 0
while i < n:
    print(a, end=" ")
    a, b = b, a + b
    i += 1
    