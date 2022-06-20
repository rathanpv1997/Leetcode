class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # n = len(nums)-1
        # l,r=1,n
        # while l<r:
        #     cnt = 0
        #     mid = (l+r)//2
        #     for num in nums:
        #         if num <= mid:
        #             cnt += 1
        #     if cnt <= mid:
        #         l = mid+1
        #     else:
        #         r = mid
        # return l
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]
        
                