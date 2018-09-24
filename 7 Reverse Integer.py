class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return x
        sign = x/abs(x)
        sol = int(str(abs(x))[::-1])
        sol *= sign
        if sol>(2**31-1) or sol<(-2**31):
            return 0
        return sol
