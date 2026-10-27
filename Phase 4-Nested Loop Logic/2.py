'''2. Print all possible pairs (i, j) where both i and j range from 1 to n.'''

n = int(input("Enter a number: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"({i}, {j})")