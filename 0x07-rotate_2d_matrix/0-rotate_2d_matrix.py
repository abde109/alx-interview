#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    # Step 1: Transpose the matrix
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()
