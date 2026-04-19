from typing import List
class Solution:

    def dfs(self , grid , r, c ):
        grid[r][c] = "0"

        lst = [ (r-1 , c) , (r+1 , c) , (r, c-1) , (r, c+1) ]

        for rw , cl in lst:
            if rw >= 0 and cl >= 0 and rw < len(grid) and cl < len(grid[rw]) and grid[rw][cl] == "1":
                self.dfs(grid , rw , cl)   

    def numIslands(self, grid :List[list[str]]) -> int:

        island = 0 

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    self.dfs(grid, r ,c)
                    island += 1
        return island


c1 = Solution()
print(c1.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))  # Output: 1