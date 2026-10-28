'''1. Print numbers from 1 to 100, and stop the loop as soon as a number divisible by 17 is encountered.'''

for i in range(1, 101):
    if i % 17 == 0:
        break
    print(i, end=" ")