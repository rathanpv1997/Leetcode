from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        c = Counter(nums)
        for num,count in c.items():
            # print(num,count)
            if count > len(nums)//2:
                return num
        