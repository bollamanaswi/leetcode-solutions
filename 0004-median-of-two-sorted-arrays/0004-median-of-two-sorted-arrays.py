class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        n = nums1 + nums2
        n.sort()

        l = len(n)
        mid = l // 2

        if l % 2 == 0:
            return (n[mid-1] + n[mid]) / 2.0
        else:
            return float(n[mid])