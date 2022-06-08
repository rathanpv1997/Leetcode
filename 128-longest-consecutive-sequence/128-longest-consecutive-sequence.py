class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = True
        cur_cnt = 1
        max_cnt = 1
        for i in d.keys():
            cur_cnt = 1
            j = i
            if j-1 not in d:
                while j+1 in d:
                    cur_cnt += 1
                    j += 1
            else:
                continue
            max_cnt = max(max_cnt, cur_cnt)
        return max_cnt
                
                
            