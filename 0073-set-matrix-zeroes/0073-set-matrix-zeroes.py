class Solution(object):

    def setZeroes(self, matrix):

        r = len(matrix)
        c = len(matrix[0])

        result = []

        # Find positions of original zeros
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    result.append((i, j))

        # Make corresponding rows and columns zero
        for i, j in result:

            # Row
            for k in range(c):
                matrix[i][k] = 0

            # Column
            for l in range(r):
                matrix[l][j] = 0
        