class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        d = {}
        nums.sort()
        
        def dfs(i):
            if i >= len(nums):
                if tuple(cur.copy()) not in d.keys():
                    res.append(cur.copy())
                    d[(tuple(cur.copy()))] = 1
                return
            
            cur.append(nums[i])
            dfs(i+1)
            cur.pop()
            # while i+1<len(nums) and nums[i] == nums[i+1]:
            #     i += 1
            dfs(i+1)
        
        dfs(0)
        return list(res)
        