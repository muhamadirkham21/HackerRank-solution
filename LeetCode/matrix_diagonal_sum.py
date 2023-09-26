class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        total = 0
        for i in range(len(mat)):
            for j in range(len(mat)):
                if (i==j or i+j == len(mat)-1):
                    total += mat[i][j]
        return total