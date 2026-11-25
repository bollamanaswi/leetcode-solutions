class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        res=""
        for char in s:
            if char.isalnum():
                res+=char
        return res==res[::-1]





        