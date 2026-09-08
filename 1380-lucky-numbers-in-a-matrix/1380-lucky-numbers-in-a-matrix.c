/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* luckyNumbers(int** matrix, int matrixSize, int* matrixColSize, int* returnSize) {
    int *result=(int*)malloc(matrixSize *sizeof(int));
    *returnSize=0;
    for(int i=0;i<matrixSize;i++){
        int col=0;
        int min=matrix[i][0];
        for(int j=1;j<matrixColSize[i];j++){
            if(matrix[i][j]<min){
                min=matrix[i][j];
                col=j;
            }

        }
        int isLucky=1;
        for(int k=0;k<matrixSize;k++){
            if(matrix[k][col]>min){
            isLucky=0;
            break;
        }
        }
        if(isLucky){
            result[*returnSize]=min;
            (*returnSize)++;
        }
    }
        return result;
}
    
    
