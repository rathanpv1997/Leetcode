class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cur_max = 1
        cur_min = 1
        for num in nums:
            if num == 0:
                cur_max, cur_min = 1,1
                continue
            tmp = cur_max*num
            cur_max = max(cur_max*num,cur_min*num,num)
            cur_min = min(tmp,cur_min*num,num)
            res = max(cur_max,res)
        return res