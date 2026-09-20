from collections import Counter
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        result=Counter(words)
        unique=list(result.keys())
        unique.sort(key=lambda x:(-result[x],x))
        return unique[:k]

        