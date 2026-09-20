class Solution(object):
    def matrixReshape(self, mat, r, c):

        rows = len(mat)
        cols = len(mat[0])

        # If total number of elements is different
        if rows * cols != r * c:
            return mat

        result = []
        k = 0

        for i in range(r):
            new_row = []

            for j in range(c):

                # Convert k into original row and column
                original_row = k // cols
                original_col = k % cols

                new_row.append(mat[original_row][original_col])

                k += 1

            result.append(new_row)

        return result