int minOperations(int n) {
     int operations = 0;

    for (int i = 0; i < n / 2; i++) {
        operations += (n - 1 - 2 * i);
    }

    return operations;
}