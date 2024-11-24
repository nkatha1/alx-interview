def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise in-place.
    Args:
        matrix (list of list of int): 2D matrix to rotate.
    """
    n = len(matrix)  # Get the size of the matrix (number of rows/columns).

    # Step 1: Transpose the matrix (convert rows to columns and vice versa).
    for i in range(n):
        for j in range(i, n):  # Only swap elements above or on the diagonal.
            # Swap elements at positions (i, j) and (j, i).
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row to complete the 90-degree rotation.
    for row in matrix:
        row.reverse()  # Reverse the row to align columns properly.

        
