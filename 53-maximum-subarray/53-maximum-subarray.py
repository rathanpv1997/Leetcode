class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        cur_sum = 0
        max_sub = nums[0]
        for i in range(n):
            cur_sum = max(nums[i],cur_sum+nums[i])
            max_sub = max(cur_sum,max_sub)
        return max_sub
    