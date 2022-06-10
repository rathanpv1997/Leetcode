class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def findpivot(nums):
            l,r =0,len(nums)-1
            while l<r:
                mid = (l+r)//2
                if nums[mid] > nums[mid+1]:
                    return mid
                elif nums[mid] > nums[r]:
                    l = mid
                else:
                    r = mid
            return -1
        if findpivot(nums) == -1: 
            return nums[0]
        else:
            return nums[findpivot(nums)+1]