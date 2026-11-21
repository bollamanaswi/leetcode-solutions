class Solution(object):
    def sumOfBeauties(self, nums):
        n = len(nums)
        
        prefix_max = [0] * n
        suffix_min = [0] * n
        
        prefix_max[0] = nums[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i-1], nums[i])
        
        suffix_min[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            suffix_min[i] = min(suffix_min[i+1], nums[i])
        
        total = 0
        
        for i in range(1, n-1):
            if prefix_max[i-1] < nums[i] and suffix_min[i+1] > nums[i]:
                total += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                total += 1
        
        return total