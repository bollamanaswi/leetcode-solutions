class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0

        l = [True] * n
        l[0] = False
        l[1] = False

        for i in range(2, int(n**0.5) + 1):
            if l[i]:
                for j in range(i*i, n, i):
                    l[j] = False

        return l.count(True)