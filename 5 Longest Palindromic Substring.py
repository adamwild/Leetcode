class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "":
            return ""
        if len(s) == 1:
            return s
        n = len(s)
        for i in range(n):
            for k in range(i+1):
                new_s = s[k:n-i+k]
                if new_s == new_s[::-1]:
                    return new_s
