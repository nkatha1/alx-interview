def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise.
    This is done in two steps:
    1. Transpose the matrix.
    2. Reverse each row.
    
    The matrix is modified in-place (no return value).
    """
    n = len(matrix)  # Get the size of the matrix (number of rows or columns)
    
    # Step 1: Transpose the matrix.
    # The transpose of a matrix is achieved by swapping elements at [i][j] and [j][i].
    # This converts rows to columns.
    for i in range(n):  # Loop over each row
        for j in range(i + 1, n):  # Loop over columns (start from i+1 to avoid re-swapping)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]  # Swap elements

    # Step 2: Reverse each row of the matrix.
    # After transposing, we need to reverse each row to complete the 90-degree rotation.
    for i in range(n):  # Loop over each row
        matrix[i].reverse()  # Reverse the elements of each row

