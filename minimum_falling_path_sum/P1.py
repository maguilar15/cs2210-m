
def fallingPathSum(A):
    n = len(A)
    matrix = [[0 for i in range(n)] for j in range(n)]

    for e in range(n): 
        matrix[0][e] = A[0][e]
        
    for i in range(n):
        for j in range(n): 
            prevVal = matrix[i-1][j]
            if j - 1 >= 0: 
                prevVal = min(prevVal, matrix[i-1][j-1])
            if j + 1 < n: 
                prevVal = min(prevVal, matrix[i-1][j+1]) 
            matrix[i][j] = prevVal + A[i][j]
    return matrix