class Solution(object):
    def deroule(self, number, string, sol):
        corr = {'2':'abc', '3':'def', '4':'ghi','5':'jkl', '6':'mno','7':'pqrs','8':'tuv','9':'wxyz' }
        if number == "":
            sol.append(string)
            return 0
        for let in corr[number[0]]:
            self.deroule(number[1:], string+let, sol)
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        sol = []
        self.deroule(digits, "", sol)
        return sol
