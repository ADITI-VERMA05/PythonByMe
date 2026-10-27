'''6. Generate and print a number triangle pattern using nested loops.'''

n = int(input("Enter the number of rows for the triangle: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  # Print a blank line after each row
