def rotate_matrix(matrix: list[list[int]]) -> None:
    """
    Rotates a given n x n matrix 90 degrees clockwise in place.
    """
    n = len(matrix)

    # Step 1: Transpose the matrix (swap rows and columns)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print("Original matrix:")
    for row in matrix:
        print(row)

    rotate_matrix(matrix)

    print("\nRotated matrix:")
    for row in matrix:
        print(row)
