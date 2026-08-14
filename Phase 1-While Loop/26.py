'''26. Find the HCF (Highest Common Factor) of two given numbers.'''

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

while num2 != 0:
    num1, num2 = num2, num1 % num2

hcf = num1
print("HCF of the two numbers is:", hcf)