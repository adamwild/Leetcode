class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        num = '-+0123456789'
        flag = False
        while not flag:
            if str == "":
                return 0
            if str[0] == ' ':
                str = str[1:]
            elif str[0] in num:
                flag = True
            else:
                return 0
        k = 1
        flag = False
        while (k < len(str)) and (str[k] in num) and not flag:
            if str[k] == "-" or str[k] == '+':
                flag = True
            else:
                k+=1
            
        if k != len(str):
            str = str[:k]
            
            
        if str == '-' or str=='+':
            return 0
            
        sol = int(str)
        if sol>(2**31-1):
            return 2**31-1
        elif sol<-(2**31):
            return -(2**31)

        return sol
