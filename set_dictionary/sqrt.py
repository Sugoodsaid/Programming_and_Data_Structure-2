def square_matrix_simple(matrix):
    # Create a new matrix with the same dimensions as the input matrix
    new_matrix = []

    for row in matrix:
        
        new_row = []
        for element in row:
            new_row.append(element ** 2)
        new_matrix.append(new_row)
    
    return new_matrix

# Example usage
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_matrix = square_matrix_simple(matrix)
print(new_matrix)  # Output: [[1, 4, 9], [16, 25, 36], [49, 64, 81]]
print(matrix)      # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
