'''5. Print the multiplication table of a given number from n × 1 to n × 10.'''

n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
    