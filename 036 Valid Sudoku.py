class Solution(object):
    def subBox(self, board, pos1, pos2):
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in range(3):
            for j in range(3):
                case = board[pos1+i][pos2+j]
                if case != '.':
                    if case not in numbers:
                        return False
                    else:
                        numbers.remove(case)
        return True
    
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        
        for i in range(3):
            for j in range(3):
                if self.subBox(board, i*3, j*3) == False:
                    return False
                
        for i in range(9):
            verif = list(numbers)
            for j in range(9):
                case = board[i][j]
                if case !='.':
                    if case not in verif:
                        return False
                    else:
                        verif.remove(case)
                        
        for i in range(9):
            verif = list(numbers)
            for j in range(9):
                case = board[j][i]
                if case !='.':
                    if case not in verif:
                        return False
                    else:
                        verif.remove(case)
                        
        return True
