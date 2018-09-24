class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        last = ""
        n = len(nums)
        i = 0
        
        while i < n:
            if i >= len(nums):
                return len(nums)
            if nums[i] != last:
                last = nums[i]
                i += 1
            else:
                nums.pop(i)
        return len(nums)
