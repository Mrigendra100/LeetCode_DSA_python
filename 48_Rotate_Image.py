
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n):
            for j in range(i ,n):
                matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]

        for row in matrix:
            row.reverse()

s1 = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
s1.rotate(matrix)
print(matrix)