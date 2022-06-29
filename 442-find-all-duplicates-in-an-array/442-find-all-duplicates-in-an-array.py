class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        # print(d)
        out = []
        for key,value in d.items():
            # print(key,value)
            if value == 2:
                out.append(key)
        return out