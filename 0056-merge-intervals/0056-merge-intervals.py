class Solution(object):

    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort(key=lambda x: x[0])

        result = []

        for i in intervals:

            if not result or result[-1][1] < i[0]:
                result.append(i)

            else:
                result[-1][1] = max(result[-1][1], i[1])

        return result