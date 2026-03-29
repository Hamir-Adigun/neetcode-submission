class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            dic={}
            for j in range(9):
                if board[i][j] in dic and ord(board[i][j])!=ord('.'):
                    return False
                dic[board[i][j]]=board[i][j]
        for i in range(9):
            dic={}
            for j in range(9):
                if board[j][i] in dic and ord(board[j][i])!=ord('.'):
                    return False
                dic[board[j][i]]=board[j][i]
        for i in range(0,9,3):
            for j in range(0,9,3):
                dic={}
                for p in range(i,i+3):
                    for q in range(j,j+3):
                        if ord(board[p][q])!=ord('.') and board[p][q] in dic :
                            return False
                        dic[board[p][q]]=board[p][q]
        return True

                
        

        