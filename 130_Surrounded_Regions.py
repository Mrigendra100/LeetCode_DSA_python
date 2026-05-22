from typing import List

class Solution:
    
    def dfs(self , board , r ,c):
        
        if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or board[r][c] != "O":
            return
        
        board[r][c] = "#"

        self.dfs(board , r-1 ,c)
        self.dfs(board , r+1 ,c)
        self.dfs(board , r ,c-1)
        self.dfs(board , r ,c+1)

         
    
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows , cols = len(board) , len(board[0])

        for r in range(rows):
            self.dfs(board , r ,0)
            self.dfs(board , r ,cols-1)

        for c in range(cols):
            self.dfs(board , 0 , c)
            self.dfs(board , rows-1 , c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "#":
                    board[r][c] = "O"

c1 = Solution()
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
c1.solve(board)        