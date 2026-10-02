'''9. Calculate and print the factorial of the given number.'''


n = int(input("Enter a number: "))
fact = 1
i = n

if n < 0:
    print("Factorial does not exist for negative numbers.")
else:
    while True:
        if i <= 1:
            break
        fact *= i
        i -= 1
    print(f"Factorial of {n} is {fact}")