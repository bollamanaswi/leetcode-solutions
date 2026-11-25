class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        v='aeiouAEIOU'
        r=[]
        for p in s:
            if p in v:
                r.append(p)
        r.sort()
        res=''
        i=0
        for p in s:
            if p in v:
                res=res+r[i]
                i=i+1
            else:
                res=res+p
        return res
        