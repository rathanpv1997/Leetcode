class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        seq = set()
        def dfs(path,t):
            if path and path not in seq:
                seq.add(path)
            for i in range(len(t)):
                dfs(path+t[i],t[:i]+t[i+1:])
                # dfs(path,t[:i]+t[i+1:])
        dfs('',tiles)
        return len(seq)