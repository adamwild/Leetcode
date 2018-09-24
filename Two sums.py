class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sol = []
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if i!= j:
                    if nums[i]+nums[j] == target:
                        sol.append(i)
                        sol.append(j)
                        return sol
