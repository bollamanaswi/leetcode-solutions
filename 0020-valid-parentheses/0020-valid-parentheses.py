class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict={")":"(","}":"{","]":"["}        
        stack=[]
        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if not stack  or stack.pop() != dict[char]:
                    return False
            
        return len(stack)==0

    