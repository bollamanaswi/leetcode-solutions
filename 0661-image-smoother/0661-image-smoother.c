int** imageSmoother(int** img, int imgSize, int* imgColSize,
                    int* returnSize, int** returnColumnSizes) {

    int m = imgSize;
    int n = imgColSize[0];

    int** result = malloc(m * sizeof(int*));
    *returnColumnSizes = malloc(m * sizeof(int));

    for (int i = 0; i < m; i++) {
        result[i] = malloc(n * sizeof(int));
        (*returnColumnSizes)[i] = n;
    }

    for (int i = 0; i < m; i++) {

        for (int j = 0; j < n; j++) {

            int sum = 0;
            int count = 0;

            for (int x = i - 1; x <= i + 1; x++) {

                for (int y = j - 1; y <= j + 1; y++) {

                    if (x >= 0 && x < m &&
                        y >= 0 && y < n) {

                        sum += img[x][y];
                        count++;
                    }
                }
            }

            result[i][j] = sum / count;
        }
    }

    *returnSize = m;
    return result;
}