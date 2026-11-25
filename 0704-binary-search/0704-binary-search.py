class Solution(object):
    def search(self, nums, target):
        low = 0
        n = len(nums)
        high = n - 1

        while low <= high:
            mid = (low + high) // 2

            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

        return -1
        