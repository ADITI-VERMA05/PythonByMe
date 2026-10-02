'''2. Print the multiplication table of a given number.'''

n = int(input("Enter a number: "))
i = 1   
while True:
    print(f"{n} x {i} = {n * i}")
    i += 1
    if i > 10:
        break