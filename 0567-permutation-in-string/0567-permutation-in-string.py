class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        h1={}
        h2={}
        if len(s1)>len(s2):
            return False
        for ch in s1:
            if ch in h1:
                h1[ch]+=1
            else:
                h1[ch]=1
        for i in range(len(s1)):
            ch=s2[i]
            if ch in h2:
                h2[ch]+=1
            else:
                h2[ch]=1
        if h1==h2:
            return True
        for i in range(len(s1),len(s2)):
            ch=s2[i]
            if ch in h2:
                h2[ch]+=1
            else:
                h2[ch]=1
            old=s2[i-len(s1)] 
            h2[old] -= 1

            if h2[old] == 0:
                del h2[old]

            # Compare both hashmaps
            if h1 == h2:
                return True

        return False
            
        