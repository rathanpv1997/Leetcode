class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        rows = len(board)
        cols = len(board[0])
        path = set()
        
        def dfs(i,r,c):
            if i == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i] or (r,c) in path:
                return False 
            path.add((r,c))
            # print(path)
            res = dfs(i+1,r-1,c) or dfs(i+1,r+1,c) or dfs(i+1,r,c-1) or dfs(i+1,r,c+1)
            path.remove((r,c))
            return res
        for r in range(rows):
            for c in range(cols):
                if dfs(0,r,c):
                    return True
        return False
            
            
            
        
            
                
           