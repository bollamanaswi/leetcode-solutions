class Solution(object):
    def reverseBits(self, n):
        ans = 0

        for i in range(32):
            bit = n & 1
            ans = (ans << 1) | bit
            n = n >> 1

        return ans
        