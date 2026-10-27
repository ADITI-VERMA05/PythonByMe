'''15. Find the LCM (Least Common Multiple) of the given numbers.'''

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Find the larger number
larger = max(num1, num2)

# Initialize LCM to the larger number
lcm = larger

# Iterate until we find a number that is divisible by both numbers
while True:
    if lcm % num1 == 0 and lcm % num2 == 0:
        break
    lcm += larger

print("LCM of", num1, "and", num2, "is:", lcm)