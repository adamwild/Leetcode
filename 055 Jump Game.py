class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)==1:
            return True
        
        max_reach = 0
        ind = -1
        while max_reach<len(nums)-1:
            ind+=1
            if ind == max_reach and nums[ind] == 0:
                return False
            
            if ind+nums[ind]>max_reach:
                max_reach = ind+nums[ind]
                
        return True
