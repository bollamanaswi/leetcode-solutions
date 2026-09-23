from collections import Counter
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=Counter(nums)
        for i in nums:
            if count[i]>1:
                return i
        