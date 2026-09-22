class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            matrix[i] = matrix[i][::-1]
        
        for i in range(n):
            for j in range(n - i):
                matrix[i][j], matrix[n - j - 1][n - i - 1] = matrix[n - j - 1][n - i - 1], matrix[i][j]
        