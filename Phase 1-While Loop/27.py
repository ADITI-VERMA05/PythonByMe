'''27. Find the LCM (Least Common Multiple) of two given numbers.'''

n1 = num1 = int(input("Enter first number: "))
n2 = num2 = int(input("Enter second number: "))

while num2 != 0:
    num1, num2 = num2, num1 % num2

hcf = num1
lcm = (n1 * n2) // hcf
print("LCM of the two numbers is:", lcm)
