int countSymmetricIntegers(int low, int high) {
    int count = 0;

    for (int i = low; i <= high; i++) {
        int n = i;
        int digits = 0;

        // Count digits
        while (n > 0) {
            digits++;
            n /= 10;
        }

        // Only even-digit numbers can be symmetric
        if (digits % 2 != 0)
            continue;

        n = i;
        int half = digits / 2;
        int sum1 = 0, sum2 = 0;

        // Sum second half
        for (int j = 0; j < half; j++) {
            sum2 += n % 10;
            n /= 10;
        }

        // Sum first half
        for (int j = 0; j < half; j++) {
            sum1 += n % 10;
            n /= 10;
        }

        if (sum1 == sum2)
            count++;
    }

    return count;
}