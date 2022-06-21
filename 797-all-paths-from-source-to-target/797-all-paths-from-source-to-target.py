class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(graph)
        
        def dfs(cur,i):
            if cur[-1] == n-1:
                res.append(cur[:])
                return
            if i == n-1:
                return
            for j in range(len(graph[i])):
                # print(graph[i][j])
                cur.append(graph[i][j])
                # print(cur,graph[i][j],res)
                dfs(cur,graph[i][j])
                cur.pop()
                
        dfs([0],0)
        return res