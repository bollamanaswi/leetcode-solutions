class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        n = len(operations)
        l1 = []

        for i in range(n):
            if operations[i].lstrip('-').isdigit():
                l1.append(int(operations[i]))

            elif operations[i] == '+':
                s = l1[-1] + l1[-2]
                l1.append(s)

            elif operations[i] == 'D':
                d = l1[-1] * 2
                l1.append(d)

            elif operations[i] == 'C':
                l1.pop()

        return sum(l1)

        