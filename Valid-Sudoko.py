# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

#SOLUTION -

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        l=[] 
        i=0 
        j=0 
        k=3 
        m=3
        r=[]
        while(k!=12): #making array of 3X3 blocks of board
            if j<k and i<m:
                r.append(board[i][j]) 
                j+=1 
            elif i==9: 
                i=0 
                j=k
                k=k+3 
                m=3
                l.append(r) 
                r=[]
            elif i==m: 
                j=k-3
                i=m 
                m+=3 
                l.append(r) 
                r=[]
            elif j==k: 
                j=k-3
                i+=1 
        l2=[] #making array for cols
        i=0 
        j=0 
        k=0 
        r2=[]
        while(j!=9): 
            if i<9:
                r2.append(board[i][j]) 
                i+=1 
            else: 
                l2.append(r2) 
                r2=[]
                j=j+1 
                i=0 
        print(l2)
        for x in range(9):  
            s=list(".123456789")
            s1=list(".123456789")
            s2=list(".123456789")
            for y in range(9): #checking l,l2,board arrays all together
                if board[x][y] in s: 
                    if board[x][y]==".":
                        f=1
                    else:
                        s.remove(board[x][y]) 
                else:
                    return False
                if l[x][y] in s1: 
                    if l[x][y]==".": 
                        f=1
                    else: 
                        s1.remove(l[x][y]) 
                else:
                    return False
                if l2[x][y] in s2: 
                    if l2[x][y]==".": 
                        f=1
                    else:
                        s2.remove(l2[x][y])
                else:
                    return False
        return True
