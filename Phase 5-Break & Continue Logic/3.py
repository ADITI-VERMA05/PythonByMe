'''3. Take 5 numbers as input, skip any number that is 0 using continue, and calculate the sum of the remaining numbers.'''

total_sum = 0

print("Please enter 5 numbers:")

for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    
    # Skip the number if it is 0
    if num == 0:
        continue
        
    total_sum += num

print(f"The sum of the remaining numbers is: {total_sum}")
