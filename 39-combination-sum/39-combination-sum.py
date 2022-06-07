class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def dfs(i, cur_sum, total):
            if total == target:
                res.append(cur_sum.copy())
                total = 0
                return
            
            if i >= len(candidates) or total > target:
                return   
            
            cur_sum.append(candidates[i])
            dfs(i, cur_sum, total+candidates[i])
            cur_sum.pop()
            dfs(i+1, cur_sum, total)
        
        dfs(0,[],0)
        return res
                