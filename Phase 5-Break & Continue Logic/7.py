'''7. Continuously add numbers in a loop and stop the loop when the sum becomes greater than 100.'''

total_sum = 0

while True:
    num = float(input("Enter a number: "))
    total_sum += num
    print(f"Current sum: {total_sum}")
    
    if total_sum > 100:
        print("Sum has exceeded 100. Stopping the loop.")
        break