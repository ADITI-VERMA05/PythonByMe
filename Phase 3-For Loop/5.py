'''5. Print the multiplication table of a given number.'''

from numpy import number
    
number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {i * number}")