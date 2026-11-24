class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        st = []
        for char in s:
            if len(st) == 0:
                st.append(char)
            else:
                if st[-1] == char:
                    st.pop()
                else:
                    st.append(char)

        return "".join(st)
