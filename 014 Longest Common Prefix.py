class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        sol = ""
        if strs == []:
            return sol
        ind = 0
        flag = True
        while flag:
            if ind>=len(strs[0]):
                return sol
            letter = strs[0][ind]
            for i in strs:
                if ind>=len(i):
                    return sol
                if i[ind] != letter:
                    flag = False
            if flag:
                sol += letter
                
            ind += 1
        
        return sol
