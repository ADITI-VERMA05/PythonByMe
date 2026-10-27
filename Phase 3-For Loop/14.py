'''14. Find the HCF (Highest Common Factor) of the given numbers.'''

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Find the smaller number
smaller = min(num1, num2)

# Initialize HCF to 1
hcf = 1

# Iterate from 1 to the smaller number
for i in range(1, smaller + 1):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i

print("HCF of", num1, "and", num2, "is:", hcf)