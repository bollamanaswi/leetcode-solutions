class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        result=[]
        n=len(mat)
        for i in range(n):
            for j in range(n):
                if (i==j or i+j==n-1):
                    result.append(mat[i][j])
        return sum(result)
        