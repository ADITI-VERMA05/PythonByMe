'''3. For every number from 1 to n, count and print the total number of its factors.'''

n = int(input("Enter a number: "))
for i in range(1, n + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    print(f"Number of factors of {i} is: {count}")