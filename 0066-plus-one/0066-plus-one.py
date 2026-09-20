class Solution(object):
    def plusOne(self, digits):

        total = 0

        for i in digits:
            total = total * 10 + i

        total += 1

        result = []

        while total > 0:
            digit = total % 10
            result.append(digit)
            total = total // 10

        result.reverse()

        return result