'''7. Print a matrix, then calculate and display the sum of each row and the sum of each column.'''

# Define the matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Print the matrix
print("Matrix:")
for row in matrix:
    print(row)

# Calculate and display the sum of each row
print("\nSum of each row:")
for i, row in enumerate(matrix):
    row_sum = sum(row)
    print(f"Row {i + 1}: {row_sum}")

# Calculate and display the sum of each column
print("\nSum of each column:")
for j in range(len(matrix[0])):
    col_sum = sum(matrix[i][j] for i in range(len(matrix)))
    print(f"Column {j + 1}: {col_sum}")