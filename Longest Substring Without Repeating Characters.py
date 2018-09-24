class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sol = 1
        if len(s) == 0:
            return 0
        for i in range(len(s)):
            sub = s[i]
            k = 1
            while i+k<len(s):
                if s[i+k] not in sub:
                    sub += s[i+k]
                else:
                    k = len(s)
                    
                if len(sub)>sol:
                    sol = len(sub)
                k += 1
        return sol
