int numPrimeArrangements(int n) {
    long long primeWays = 1;
    long long nonPrimeWays = 1;
    int primeCount = 0;
    int MOD = 1000000007;

    // Count prime numbers
    for (int i = 2; i <= n; i++) {
        int isPrime = 1;

        for (int j = 2; j * j <= i; j++) {
            if (i % j == 0) {
                isPrime = 0;
                break;
            }
        }

        if (isPrime) {
            primeCount++;
        }
    }

    // primeCount!
    for (int i = 1; i <= primeCount; i++) {
        primeWays = (primeWays * i) % MOD;
    }

    // (n - primeCount)!
    for (int i = 1; i <= n - primeCount; i++) {
        nonPrimeWays = (nonPrimeWays * i) % MOD;
    }

    return (primeWays * nonPrimeWays) % MOD;
}