class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
     
        """
        if x<0:
         return False
        target=0
        original =x
    
        while(x>0):
           remainder=x%10
           target=(target*10)+remainder
           x=x//10
           
        if original==target:
            return True
        else:
            return False
