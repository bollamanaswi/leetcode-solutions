class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        st = []

        for char in s:
            if len(st) == 0:
                st.append([char, 1])

            elif st[-1][0] == char:
                st[-1][1] += 1

                if st[-1][1] == k:
                    st.pop()

            else:
                st.append([char, 1])

        result = ""

        for char, count in st:
            result += char * count

        return result

        