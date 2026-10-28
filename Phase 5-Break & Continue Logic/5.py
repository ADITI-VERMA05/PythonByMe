'''5. Keep taking numbers from the user and print them until a negative number appears, then stop the loop.'''

while True:
    num = float(input("Enter a number: "))
    print(f"You entered: {num}")
    
    if num < 0:
        print("Negative number detected. Stopping the loop.")
        break