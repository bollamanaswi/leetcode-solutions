class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=max(nums)
        b=min(nums)
        n=len(nums)
        for i in range(0,n):
            if nums[i]!= a and nums[i]!=b:
                return nums[i]
        return -1        