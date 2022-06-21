class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        d = [[0]*cols]*rows
        cnt = 0
        self.res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != -1:
                    cnt += 1
                if grid[r][c] == 1:
                    x,y = r,c
                           
        def dfs(empty,r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] < 0:
                return
            empty += 1
            if grid[r][c] == 2 and empty!=cnt:
                return
            # print(empty)
            if empty == cnt:
                self.res += 1
                return      
            grid[r][c] = -2     
            
            dfs(empty,r+1,c)
            dfs(empty,r-1,c)
            dfs(empty,r,c+1)
            dfs(empty,r,c-1)
            grid[r][c] = 0
        dfs(0,x,y)
        return self.res
            
            