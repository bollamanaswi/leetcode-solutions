int gcd(int a, int b)
{
    while (b != 0)
    {
        int temp = b;
        b = a % b;
        a = temp;
    }

    return a;
}

int lcm(int a, int b)
{
    return (a / gcd(a, b)) * b;
}

int subarrayLCM(int* nums, int numsSize, int k)
{
    int count = 0;

    for (int i = 0; i < numsSize; i++)
    {
        int currentLCM = 1;

        for (int j = i; j < numsSize; j++)
        {
            currentLCM = lcm(currentLCM, nums[j]);

            if (currentLCM == k)
            {
                count++;
            }

            if (currentLCM > k)
            {
                break;
            }
        }
    }

    return count;
}