class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            return 0 if nums[0] == target else -1
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
        def search(nums,l,r,target):
            while l<=r:
                mid = (l+r)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid-1
                else:
                    l = mid+1
            return -1
           
        pivot_index = findpivot(nums)
        if pivot_index == -1:
            return search(nums,0,n-1,target)
        pivot_num = nums[pivot_index]
        if target > pivot_num:
            return -1
        if nums[0] <= target <= pivot_num:
            return search(nums,0,pivot_index,target)
        else:
            return search(nums,pivot_index+1,n-1,target)
        
            
                
                    