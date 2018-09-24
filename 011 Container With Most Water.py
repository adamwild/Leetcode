class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        ind1 = 0
        ind2 = n-1
        v1 = height[ind1]
        v2 = height[ind2]
        vol = abs(ind1-ind2)*min(v1,v2)
        
        while ind1 != ind2:
            if v2<v1:
                ind2-=1
                v2 = height[ind2]
            else:
                ind1 += 1
                v1 = height[ind1]
            if abs(ind1-ind2)*min(v1,v2)>vol:
                vol = abs(ind1-ind2)*min(v1,v2)
        return vol
