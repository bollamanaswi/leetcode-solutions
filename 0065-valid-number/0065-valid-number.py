class Solution(object):
    def isNumber(self, s):
        try:
            float(s)
            if 'inf' in s.lower() or 'nan' in s.lower():
                return False
            return True
        except:
            return False