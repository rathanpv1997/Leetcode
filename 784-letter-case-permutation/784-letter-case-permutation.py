class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        n = len(s)
        # visited = set()
        
        def dfs(i,sub):
            if i == n:
                res.append(sub[:])
            else:
                if s[i].isalpha():
                    dfs(i+1,sub + s[i].swapcase())
                dfs(i+1,sub + s[i])
        dfs(0,"")
        return res