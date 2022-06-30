class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        def dfs(i,path):
            if len(path) > k or sum(path) > n or i>9:
                return
            if len(path) == k and sum(path) == n:
                res.append(path[:])
                return
            path.append(i+1)
            # print(path)
            dfs(i+1,path)
            path.pop()
            dfs(i+1,path)
        
        # for i in range(7):
        #     dfs(i,[])
        dfs(0,[])
        return res
            