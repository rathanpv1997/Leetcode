class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        forward = [1]*n
        backward = [1]*n
        forward[0] = nums[0]
        backward[n-1] = nums[n-1]
        for i in range(1,n):
            forward[i] = nums[i]*forward[i-1]
            backward[n-i-1] = nums[n-i-1]*backward[n-i]
        out = [0]*n
        out[0] = backward[1]
        out[n-1] = forward[n-1-1]
        # print(forward,backward)
        for i in range(1,n-1):
            out[i] = forward[i-1]*backward[i+1]
        return out