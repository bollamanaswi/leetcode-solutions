#include <stdlib.h>

int countDigits(int x) {
    int count = 0;

    if (x == 0)
        return 1;

    if (x < 0) {
        count++;       // Count '-' sign
        x = -x;
    }

    while (x > 0) {
        count++;
        x /= 10;
    }

    return count;
}

int* findColumnWidth(int** grid, int gridSize, int* gridColSize, int* returnSize) {
    
    int n = gridColSize[0];   // Number of columns

    int* ans = (int*)malloc(n * sizeof(int));

    *returnSize = n;

    for (int j = 0; j < n; j++) {
        ans[j] = 0;

        for (int i = 0; i < gridSize; i++) {
            int length = countDigits(grid[i][j]);

            if (length > ans[j]) {
                ans[j] = length;
            }
        }
    }

    return ans;
}