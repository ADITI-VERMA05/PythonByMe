'''2. Print numbers from 1 to 100, but skip all numbers that are divisible by 5 and continue printing the rest.'''

for i in range(1, 101):
    if i % 5 == 0:
        continue
    print(i, end=" ")