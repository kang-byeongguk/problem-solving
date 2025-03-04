class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        low=len(board)
        column=len(board[0])

        def isTrue(m,n,word_index):
            if not (0 <= m < low and 0<= n < column):
                return False
            if board[m][n]==word[word_index]:
                return True
            return False
        
        def backtrack(m,n,word_index):
            direction=[(0,1),(0,-1),(-1,0),(1,0)]
            if word_index==len(word):
                return True

            if isTrue(m,n,word_index):
                tmp=board[m][n]
                board[m][n]='#'
                found=False
                for dm,dn in direction:
                    if backtrack(m+dm,n+dn,word_index+1):
                        found=True
                board[m][n]=tmp
                return found
            return False
        for m in range(low):
            for n in range(column):
                if backtrack(m,n,0):
                    return True
        return False

