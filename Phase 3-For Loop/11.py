'''11. Find and print the sum of the Fibonacci series.'''

def sum_fibonacci(n):
    # Handle edge case for invalid inputs
    if n <= 0:
        print("Please enter a positive integer.")
        return 0
        
    n1, n2 = 0, 1
    total_sum = 0
    
    # Use a for loop to iterate exactly 'n' times
    for _ in range(n):
        total_sum += n1
        # Update n1 to the next element and n2 to the sum
        n1, n2 = n2, n1 + n2
    
    return total_sum