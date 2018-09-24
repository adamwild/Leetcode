class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n<0:
            x = 1/x
            n = -n
            
        if n == 1:
            return x
        elif n == 0:
            return 1

        elif n%2 == 1:
            return x*self.myPow(x, n-1)
        else:
            return self.myPow(x*x,n/2)
