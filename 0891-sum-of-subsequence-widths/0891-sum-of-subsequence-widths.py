class Solution(object):
    def sumSubseqWidths(self, nums):
        nums.sort()
        n = len(nums)
        mod = 10**9 + 7

        ans = 0
        power = 1

        for i in range(n):
            ans = (ans + nums[i] * (power - 1)) % mod
            ans = (ans - nums[i] * (pow(2, n-1-i, mod) - 1)) % mod
            power = (power * 2) % mod

        return ans
        