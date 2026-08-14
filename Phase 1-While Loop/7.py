'''7. Calculate the sum of all even numbers from 1 up to n.'''

n = int(input("Enter a number: "))
sum = 0
for i  in range(2, n + 1, 2):
    sum += i
print(f"The sum of all even numbers from 1 up to {n} is: {sum}")
