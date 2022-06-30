class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        res = []
        n = len(nums)
        nums.sort()
        
        def dfs(i,path):
            if i == n:
                res.append(path[:])
                return
            
            dfs(i+1,path+[nums[i]])
            while i+1<n and nums[i] == nums[i+1]:
                i = i + 1
            dfs(i+1,path)
        dfs(0,[])
        return res
        