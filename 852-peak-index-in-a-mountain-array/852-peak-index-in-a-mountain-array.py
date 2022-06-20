class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l,r=0,len(arr)-1
        while l<r-1:
            mid = (l+r)//2
            if arr[mid-1]<arr[mid]>arr[mid+1]:
                return mid
            elif arr[mid-1]<arr[mid]:
                l = mid
            else:
                r = mid
        return mid