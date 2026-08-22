char* baseNeg2(int n) {
    char* result = (char*)malloc(40 * sizeof(char));
    int index = 0;

    if (n == 0) {
        result[0] = '0';
        result[1] = '\0';
        return result;
    }

    while (n != 0) {
        int remainder = n % (-2);
        n /= -2;

        if (remainder < 0) {
            remainder += 2;
            n++;
        }

        result[index++] = remainder + '0';
    }

    result[index] = '\0';

    // Reverse the string
    for (int i = 0, j = index - 1; i < j; i++, j--) {
        char temp = result[i];
        result[i] = result[j];
        result[j] = temp;
    }

    return result;
}