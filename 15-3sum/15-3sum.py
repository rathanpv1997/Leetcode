class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums)<3:
            return []
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j,k=i+1,n-1
            while j<k:
                three_sum = nums[i]+nums[j]+nums[k]
                if three_sum == 0:
                    res.append([nums[i],nums[j],nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j+=1
                    k-=1
                if three_sum < 0:
                    j += 1
                if three_sum > 0:
                    k -= 1
        return res