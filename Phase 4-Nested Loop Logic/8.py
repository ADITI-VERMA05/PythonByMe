'''8. Print all Pythagorean triplets whose values are less than or equal to n.'''

n = int(input("Enter a number: "))
print(f"Pythagorean triplets up to {n} are:")
for a in range(1, n + 1):
    for b in range(a, n + 1):
        for c in range(b, n + 1):
            if a**2 + b**2 == c**2:
                print(f"({a}, {b}, {c})")