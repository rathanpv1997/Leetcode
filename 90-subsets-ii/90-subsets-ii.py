class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        
        nums.sort()
        
        def dfs(i):
            if i >= len(nums):
                res.append(cur.copy()) if cur not in res else res
                return
            
            cur.append(nums[i])
            dfs(i+1)
            cur.pop()
            dfs(i+1)
        
        dfs(0)
        return list(res)
        