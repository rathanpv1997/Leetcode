class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(graph)
        
        def dfs(cur,i):
            # if cur[-1] == n-1:
            #     res.append(cur[:])
            #     return
            if i == n-1:
                res.append(cur)
                return
            for j in graph[i]:
                dfs(cur + [j], j)
                
        dfs([0],0)
        return res