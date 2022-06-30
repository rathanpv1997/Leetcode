class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        res = []
        n = len(nums)
        def dfs(i,path):
            if i == n:
                res.append(path[:])
                return
            dfs(i+1,path+[nums[i]])
            dfs(i+1,path)
        dfs(0,[])
        return res