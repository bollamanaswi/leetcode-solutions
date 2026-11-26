class Solution(object):
    def minEatingSpeed(self, piles, h):
        low = 1
        high = max(piles)

        while low < high:
            mid = (low + high) // 2
            t = 0

            for p in piles:
                t += (p + mid - 1) // mid

            if t <= h:
                high = mid
            else:
                low = mid + 1

        return low