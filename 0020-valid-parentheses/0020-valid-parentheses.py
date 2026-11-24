class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []
        r = '[{('

        for p in s:
            if p in r:
                st.append(p)

            elif (st and (st[-1] == '[' and p == ']' or
                          st[-1] == '(' and p == ')' or
                          st[-1] == '{' and p == '}')):
                st.pop()

            else:
                return False

        if st:
            return False
        else:
            return True