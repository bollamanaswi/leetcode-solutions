class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
    
        original_num=x
        x=abs(x)
        total=0
        while x >0:
            remainder=x%10
            if total > (2**31 - 1) // 10 or (total == (2**31 - 1) // 10 and remainder > 7):
                return 0
            total=(total*10)+remainder
            x=x//10
        if original_num <0:
            return -total
        if x < -2**31 or x>2**31-1:
            return 0
        else:
            return total


        