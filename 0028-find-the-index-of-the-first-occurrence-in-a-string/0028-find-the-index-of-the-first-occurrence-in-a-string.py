class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        m=len(haystack)
        n=len(needle)
        for i in range(m):
            if haystack[i]==needle[0]:
                j=0
                while j<n and i+j<m and haystack[i+j]==needle[j]:
                    j+=1
                if j==n:
                    return i
        return -1
        