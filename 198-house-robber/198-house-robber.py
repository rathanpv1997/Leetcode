class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        dp = nums[:]
        dp[1] = max(nums[0],nums[1])
        
        for i in range(2,n):
            dp[i] = max(nums[i]+dp[i-2],dp[i-1])
        
        return dp[-1]
        
    # def rob(self, A):
    #     if len(A) == 1: return A[0]
    #     dp = [*A]
    #     dp[1] = max(A[0], A[1])
    #     for i in range(2, len(A)):
    #         dp[i] = max(dp[i-1], A[i] + dp[i-2])
    #     return dp[-1]