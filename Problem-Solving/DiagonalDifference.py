def diagonalDifference(arr):
    # Write your code here
    left_diagonal = 0
    right_diagonal = 0
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if i == j:
                left_diagonal += arr[i][j]
            if i + j == n - 1 :
                right_diagonal += arr[i][j]
    
    if left_diagonal > right_diagonal:
        return left_diagonal-right_diagonal
    else:
        return right_diagonal-left_diagonal

arr = [
    [1, 2, 3],
    [4, 5, 6],
    [9, 8, 9]
]

print(diagonalDifference(arr))