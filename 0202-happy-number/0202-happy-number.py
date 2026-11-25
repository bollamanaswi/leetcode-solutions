class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s=set()
        
        while(n!=1):
            if n not in s:
                s.add(n)
            else:
                return False
            total=0
            while(n>=1):
                r=n%10
                total=total+(r*r)
                n=n//10
            n=total
        return True
 
        
        