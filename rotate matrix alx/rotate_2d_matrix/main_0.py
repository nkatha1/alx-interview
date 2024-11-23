#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
# Importing the function 'rotate_2d_matrix' from the file '0-rotate_2d_matrix.py'
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    # Test matrix: A 3x3 matrix to test the rotation.
    matrix = [[1, 2, 3],   # First row
              [4, 5, 6],   # Second row
              [7, 8, 9]]   # Third row

    # Call the rotate function to rotate the matrix 90 degrees clockwise.
    rotate_2d_matrix(matrix)

    # Print the rotated matrix to check the result.
    print(matrix)
