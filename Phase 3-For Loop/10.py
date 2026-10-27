'''10. Print the Fibonacci series up to the required number of terms.'''

def print_fibonacci_for_loop(n):
    # Handle edge case for invalid inputs
    if n <= 0:
        print("Please enter a positive integer.")
        return
        
    n1, n2 = 0, 1
    print(f"Fibonacci sequence up to {n} terms:")
    
    # Use a for loop to iterate exactly 'n' times
    for _ in range(n):
        print(n1, end=" ")
        # Update n1 to the next element and n2 to the sum
        n1, n2 = n2, n1 + n2
    print()  # For a clean line break

# Get user input
try:
    terms = int(input("Enter the number of terms: "))
    print_fibonacci_for_loop(terms)
except ValueError:
    print("Invalid input! Please enter an integer.")
