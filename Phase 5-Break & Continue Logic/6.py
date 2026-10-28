'''6. Skip all odd numbers and print only the even numbers.'''

while True:
    num = float(input("Enter a number (or type 'exit' to stop): "))
    
    if isinstance(num, str) and num.lower() == 'exit':
        print("Exiting the loop.")
        break
    
    if num % 2 != 0:
        continue  # Skip odd numbers
    
    print(f"You entered an even number: {num}")