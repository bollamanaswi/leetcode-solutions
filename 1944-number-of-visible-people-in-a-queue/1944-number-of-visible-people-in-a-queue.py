class Solution(object):
    def canSeePersonsCount(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        st=[]
        n=len(heights)
        r=[0]*n
        for p in range (n-1,-1,-1):
            while(st and heights[st[-1]]<heights[p]):
                st.pop()
                r[p]=r[p]+1
            if st:
                r[p]=r[p]+1
            st.append(p)
        return r

        