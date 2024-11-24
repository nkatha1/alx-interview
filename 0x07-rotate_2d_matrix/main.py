#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
# Import the function from the solution file
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    # Define a sample 3x3 matrix to test
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    # Call the function to rotate the matrix
    rotate_2d_matrix(matrix)

    # Print the rotated matrix to check the result
    print(matrix)
