void setZeroes(int** matrix, int matrixSize, int* matrixColSize) {
    int rows = matrixSize;
    int cols = matrixColSize[0];

    int zeroRow[rows];
    int zeroCol[cols];

    // Initially, no row or column contains zero
    for (int i = 0; i < rows; i++) {
        zeroRow[i] = 0;
    }

    for (int j = 0; j < cols; j++) {
        zeroCol[j] = 0;
    }

    // Find all rows and columns containing 0
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {

            if (matrix[i][j] == 0) {
                zeroRow[i] = 1;
                zeroCol[j] = 1;
            }
        }
    }

    // Set complete rows to 0
    for (int i = 0; i < rows; i++) {
        if (zeroRow[i] == 1) {
            for (int j = 0; j < cols; j++) {
                matrix[i][j] = 0;
            }
        }
    }

    // Set complete columns to 0
    for (int j = 0; j < cols; j++) {
        if (zeroCol[j] == 1) {
            for (int i = 0; i < rows; i++) {
                matrix[i][j] = 0;
            }
        }
    }
}