int minOperations(int* nums, int numsSize) {

    int count[1000001] = {0};
    int operations = 0;

    // Count frequency of each number
    for (int i = 0; i < numsSize; i++) {
        count[nums[i]]++;
    }

    // Process each number
    for (int i = 1; i <= 1000000; i++) {

        if (count[i] == 0)
            continue;

        // Frequency 1 cannot be removed
        if (count[i] == 1)
            return -1;

        // Use groups of 3 as much as possible
        operations += count[i] / 3;

        // If remainder is 1, replace one group of 3
        // with two groups of 2
        if (count[i] % 3 == 1) {
            operations--;
            operations += 2;
        }

        // Remainder 2 needs one group of 2
        else if (count[i] % 3 == 2) {
            operations++;
        }
    }

    return operations;
}