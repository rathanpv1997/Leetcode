class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # if not nums1 and not nums2:
        # return -1.0

        m = len(nums1)
        n = len(nums2)

        merge_arr = []

        if nums1 and nums2:
            if nums1[0]>=nums2[-1]:
                merge_arr.extend(nums2)
                merge_arr.extend(nums1)

            elif nums2[0]>=nums1[-1]:
                merge_arr.extend(nums1)
                merge_arr.extend(nums2)

            else:
                i,j = 0,0
                while i<m and j<n:
                    if nums1[i]<nums2[j]:
                        merge_arr.append(nums1[i])
                        i += 1
                    elif nums1[i]>nums2[j]:
                        merge_arr.append(nums2[j])
                        j += 1
                    else:
                        merge_arr.append(nums2[j])
                        merge_arr.append(nums1[i])
                        i += 1
                        j += 1
                if i != m:
                    merge_arr.extend(nums1[i:m])
                if j != n:
                    merge_arr.extend(nums2[j:n])
                    
        else:
            if nums1 and not nums2:
                merge_arr = nums1
            if nums2 and not nums1:
                merge_arr = nums2
        print(merge_arr)
        k = m+n
        if k == 1:
            return merge_arr[0]*1.0
        if k % 2 == 0:
            return (merge_arr[k//2]+merge_arr[k//2-1])/2
        else:
            return merge_arr[k//2]*1.0