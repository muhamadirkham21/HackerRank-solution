class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        dummyRow = [-1] * row
        dummyCol = [-1] * col

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    dummyRow[i] = 0
                    dummyCol[j] = 0
        
        for i in range(row):
            for j in range(col):
                if dummyRow[i] == 0 or dummyCol[j] == 0:
                    matrix[i][j] == 0
