int** findPrimePairs(int n, int* returnSize, int** returnColumnSizes)
{
    // prime[i] = 1 means i is prime
    int *prime = malloc((n + 1) * sizeof(int));

    for (int i = 0; i <= n; i++)
        prime[i] = 1;

    prime[0] = 0;
    prime[1] = 0;

    // Sieve
    for (int i = 2; i * i <= n; i++)
    {
        if (prime[i])
        {
            for (int j = i * i; j <= n; j += i)
            {
                prime[j] = 0;
            }
        }
    }

    // Maximum possible number of pairs is n/2
    int **result = malloc((n / 2 + 1) * sizeof(int *));
    *returnColumnSizes = malloc((n / 2 + 1) * sizeof(int));

    *returnSize = 0;

    // Find pairs
    for (int x = 2; x <= n / 2; x++)
    {
        int y = n - x;

        if (prime[x] && prime[y])
        {
            result[*returnSize] = malloc(2 * sizeof(int));

            result[*returnSize][0] = x;
            result[*returnSize][1] = y;

            (*returnColumnSizes)[*returnSize] = 2;
            (*returnSize)++;
        }
    }

    free(prime);

    return result;
}