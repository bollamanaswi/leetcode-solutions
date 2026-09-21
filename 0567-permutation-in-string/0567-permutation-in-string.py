class Solution(object):

    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        if len(s1) > len(s2):
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        # Count characters of s1
        for ch in s1:
            count1[ord(ch) - ord('a')] += 1

        # First window of s2
        for i in range(len(s1)):
            count2[ord(s2[i]) - ord('a')] += 1

        # Check the first window
        if count1 == count2:
            return True

        # Slide the window
        for i in range(len(s1), len(s2)):

            # Add new character
            count2[ord(s2[i]) - ord('a')] += 1

            # Remove old character
            count2[ord(s2[i - len(s1)]) - ord('a')] -= 1

            # Compare frequencies
            if count1 == count2:
                return True

        return False

        