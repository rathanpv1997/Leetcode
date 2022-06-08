class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        num_set = set(nums)
        cur_cnt = 1
        max_cnt = 1
        for num in nums:
            cur_cnt = 1
            if num-1 not in num_set:
                while num+1 in num_set:
                    cur_cnt += 1
                    num += 1
            max_cnt = max(max_cnt, cur_cnt)
        return max_cnt
                
                
            