class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        st = []
        maxi = 0
        n = len(heights)

        for i in range(n):
            while(st and heights[st[-1]] > heights[i]):
                h = heights[st.pop()]

                if st:
                    w = i - st[-1] - 1
                else:
                    w = i

                maxi = max(maxi, h * w)

            st.append(i)

        while(st):
            h = heights[st.pop()]

            if st:
                w = n - st[-1] - 1
            else:
                w = n

            maxi = max(maxi, h * w)

        return maxi
        