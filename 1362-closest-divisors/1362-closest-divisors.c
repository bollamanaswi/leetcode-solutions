int* closestDivisors(int num, int* returnSize)
{
    int *ans = malloc(2 * sizeof(int));
    *returnSize = 2;

    int bestDiff = num + 2;

    for (int n = num + 1; n <= num + 2; n++)
    {
        for (int i = 1; i * i <= n; i++)
        {
            if (n % i == 0)
            {
                int j = n / i;
                int diff = j - i;

                if (diff < bestDiff)
                {
                    bestDiff = diff;
                    ans[0] = i;
                    ans[1] = j;
                }
            }
        }
    }

    return ans;
}