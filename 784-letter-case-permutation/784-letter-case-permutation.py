class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        n = len(s)
        visited = set()
        
        def dfs(i,path):
            if i == n:
                if path not in visited:
                    res.append(path[:])
                    visited.add(path[:])
                    return
                else:
                    return
            dfs(i+1,path+s[i].lower())
            dfs(i+1,path+s[i].upper())
        dfs(0,"")
        return res