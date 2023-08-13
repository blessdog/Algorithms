'''
You're given a 2D array of integers--> "MATRIX". 
Write a function that returns the transpose of the matrix.

The transpose of a matrix is a flipped version of the oiriginal matrix across its main diagonal 
(which runs from top-left to bottom-right);
it switches the row and column indices of the original matrix. 

You can assume the input matrix always has at least 1 value; 
however its width and height are not necessaryly the same.
'''
def transpose_matris(matrix):
# Get the dimensions of the input matrix
    rows = len(matrix)
    columns = len(matrix[0] if rows > 0 else 0)

    # Create a new matrix to store the transposed values
    transposed = 
def transpose_matrix(original_matrix):
    original_rows = len(original_matrix)
    original_cols = len(original_matrix[0]) if original_rows > 0 else 0
    
    transposed_rows = original_cols
    transposed_cols = original_rows
    
    transposed_matrix = [[0] * transposed_cols for _ in range(transposed_rows)]
    
    for i in range(original_rows):
        for j in range(original_cols):
            transposed_matrix[j][i] = original_matrix[i][j]
    
    return transposed_matrix

