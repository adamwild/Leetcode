class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        bas = 0
        haut = x
        while haut-bas != 1:
            mil = (haut+bas)/2
            if mil**2>x:
                haut = mil
            elif mil**2 == x:
                return int(mil)
            else:
                bas = mil
        return int(bas)
