'''7. Calculate and print the factorial of every number from 1 to n.'''

for i in range(1, n + 1):
    factorial = 1
    for j in range(1, i + 1):
        factorial *= j
    print(f"The factorial of {i} is {factorial}")